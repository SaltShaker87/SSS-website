// Renders figures from paper.json. Never computes or invents values: reads numbers[] by id.
(function(){
 const C={a:'#ffd23f',b:'#1f82e0',n:'#586173',edge:'#141a24'};
 const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 window.renderPaperCharts=function(p){
  const byId=Object.fromEntries(p.numbers.map(n=>[n.id,n]));
  const fv=n=>n.value==null?'—':(n.decimals!=null?Number(n.value).toFixed(n.decimals):n.value);
  if(window.Chart){Chart.defaults.font.family='"IBM Plex Sans",system-ui,sans-serif';Chart.defaults.color='#141a24';}
  // Any visible pixel counts. A 30% rule never fires for a window taller than the screen,
  // which hid the whole results section and every chart on this page.
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');e.target._draw&&e.target._draw();io.unobserve(e.target);}}),{threshold:0});
  document.querySelectorAll('.reveal').forEach(el=>{io.observe(el);});
  p.figures.forEach(f=>{
   const fig=document.querySelector(`[data-figure="${f.id}"]`); if(!fig) return;
   const nums=f.number_ids.map(id=>byId[id]||{id,label:id,value:null,status:'MISSING'});
   const tbl=fig.querySelector('table.data');
   tbl.innerHTML='<tr><th>Label</th><th>Value</th><th>95% CI</th><th>Status</th></tr>'+nums.map(n=>`<tr><td>${n.label}</td><td>${fv(n)}${n.unit||''}</td><td>${n.ci_low!=null?n.ci_low+' to '+n.ci_high:''}</td><td>${n.status}</td></tr>`).join('');
   if(nums.some(n=>n.status!=='VERIFIED')){fig.insertAdjacentHTML('afterbegin','<div class="missing">⚠ data needed: some values are missing or unverified</div>');}
   const cv=fig.querySelector('canvas'); const ok=nums.filter(n=>typeof n.value==='number');
   const draw=()=>{
    const anim=reduce?false:{duration:1200,easing:'easeOutQuart'};
    if(f.type==='bar'||f.type==='donut'){
     new Chart(cv,{type:f.type==='bar'?'bar':'doughnut',data:{labels:(f.series_labels&&f.series_labels.length===ok.length)?f.series_labels:ok.map(n=>n.label),datasets:[{data:ok.map(n=>n.value),backgroundColor:ok.map((_,i)=>[C.a,C.b,C.n][i%3]),borderColor:C.edge,borderWidth:2}]},options:{animation:anim,aspectRatio:innerWidth<600?1.2:2.4,plugins:{legend:{display:f.type!=='bar'}},scales:f.type==='bar'?{y:{beginAtZero:true,title:{display:!!f.y_label,text:f.y_label}}}:{}}});
    }else if(f.type==='grouped'&&f.groups){
     // groups: [{label, ids:[armA, armB]}]; series_labels name the arms. Missing values become gaps, never zeros.
     const arms=f.series_labels||['A','B'];
     new Chart(cv,{type:'bar',data:{labels:f.groups.map(g=>g.label),datasets:arms.map((a,i)=>({label:a,data:f.groups.map(g=>{const n=byId[g.ids[i]];return n&&n.status==='VERIFIED'?n.value:null;}),backgroundColor:[C.a,C.b][i%2],borderColor:C.edge,borderWidth:2}))},options:{animation:anim,aspectRatio:innerWidth<600?1:2.4,plugins:{legend:{display:true}},scales:{y:{beginAtZero:true,title:{display:!!f.y_label,text:f.y_label}}}}});
    }else if(f.type==='forest'){
     // margin line drawn only if f.margin_id points to a VERIFIED number; never assumed
     const mgN=f.margin_id&&byId[f.margin_id]?.status==='VERIFIED'?byId[f.margin_id]:null;const mg=mgN?{value:mgN.value*(f.margin_direction||1)}:null; // margin_direction:-1 draws a +10 margin at -10
     const vals=ok.flatMap(n=>[n.value,n.ci_low,n.ci_high]).concat([0,mg?mg.value:0]).filter(v=>typeof v==='number');const pad=(Math.max(...vals)-Math.min(...vals))*.15||1;const xr=[Math.floor(Math.min(...vals)-pad),Math.ceil(Math.max(...vals)+pad)];
     cv.parentElement.style.height=Math.max(140,60+ok.length*50)+'px';
     new Chart(cv,{type:'scatter',data:{datasets:[{data:ok.map((n,i)=>({x:n.value,y:i})),pointRadius:7,backgroundColor:C.a,borderColor:C.edge}]},options:{animation:anim,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{enabled:false}},scales:{x:{min:xr[0],max:xr[1],title:{display:!!f.y_label,text:f.y_label}},y:{ticks:{stepSize:1,callback:v=>ok.length>1?((f.series_labels||[])[v]||ok[v]?.label||''):''},reverse:true,min:-1,max:ok.length}}},plugins:[{id:'ci',afterDatasetsDraw(c){const x=c.scales.x,y=c.scales.y,g=c.ctx;g.save();const vline=(v,col,dash)=>{g.strokeStyle=col;g.setLineDash(dash);g.lineWidth=2;g.beginPath();g.moveTo(x.getPixelForValue(v),y.top);g.lineTo(x.getPixelForValue(v),y.bottom);g.stroke();g.setLineDash([]);};vline(0,C.n,[4,4]);if(mg){vline(mg.value,'#b91c1c',[8,4]);g.fillStyle='#b91c1c';g.font='600 12px "IBM Plex Sans"';g.fillText('NI margin',x.getPixelForValue(mg.value)+4,y.top+12);}g.strokeStyle=C.edge;g.lineWidth=2;ok.forEach((n,i)=>{if(n.ci_low==null)return;g.beginPath();g.moveTo(x.getPixelForValue(n.ci_low),y.getPixelForValue(i));g.lineTo(x.getPixelForValue(n.ci_high),y.getPixelForValue(i));g.stroke();});g.restore();}}]});
    }else if(f.type==='km'&&f.km_points?.length){
     const arms=[...new Set(f.km_points.map(p=>p.arm))];
     new Chart(cv,{type:'line',data:{datasets:arms.map((a,i)=>({label:a,data:f.km_points.filter(p=>p.arm===a).map(p=>({x:p.t,y:p.y})),stepped:true,borderColor:[C.a,C.b][i%2],borderWidth:3,pointRadius:0}))},options:{animation:anim,parsing:false,scales:{x:{type:'linear'}}}});
    }else if(f.type==='bignumber'&&ok[0]){
     const d=document.createElement('div');d.className='stat';d.innerHTML=`<b>0</b><span>${ok[0].label}</span>`;cv.replaceWith(d);
     const b=d.querySelector('b'),t=ok[0].value,u=ok[0].unit||'',dec=(String(t).split('.')[1]||'').length;
     if(reduce){b.textContent=t+u;return;} let s=null;const step=ts=>{s??=ts;const k=Math.min(1,(ts-s)/1200);b.textContent=(t*k).toFixed(dec)+u;if(k<1)requestAnimationFrame(step);};requestAnimationFrame(step);
    }
   };
   // Draw when this chart scrolls into view, not when the whole section does.
   fig._draw=draw; io.observe(fig);
  });
 };
})();
