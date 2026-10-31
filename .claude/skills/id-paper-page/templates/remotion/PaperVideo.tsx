// Deterministic hero video. All numbers come from paper.json props; no hardcoded data.
import {AbsoluteFill, Sequence, cancelRender, continueRender, delayRender, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
// Hold every frame until the site fonts load. Without this Remotion renders a serif fallback.
const fonts=delayRender('site fonts');const css=document.createElement('link');css.rel='stylesheet';
css.href='https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@700&family=IBM+Plex+Sans:wght@500;600&display=block';
css.onload=()=>Promise.all(['700 16px "Pixelify Sans"','500 16px "IBM Plex Sans"','600 16px "IBM Plex Sans"'].map(f=>document.fonts.load(f))).then(()=>continueRender(fonts)).catch(cancelRender);
css.onerror=()=>cancelRender(new Error('Could not load site fonts'));document.head.appendChild(css);
type Num={id:string;label:string;value:number|string|null;unit?:string;status:string;decimals?:number};
type Paper={citation:{title:string;short_name?:string;journal:string;year:number};numbers:Num[];hero_findings:{number_id:string;headline:string}[];sections:{practice_impact?:string}};
const C={deskA:'#117178',deskB:'#0a4650',face:'#eef0f3',edge:'#141a24',salt:'#ffd23f',blue:'#1f82e0',titleA:'#0b1f8f'};
const Win:React.FC<{title:string;children:React.ReactNode}>=({title,children})=>{const f=useCurrentFrame(),{fps}=useVideoConfig();const s=spring({frame:f,fps,config:{damping:12}});
 return <div style={{transform:`scale(${s})`,background:C.face,border:`4px solid ${C.edge}`,borderRadius:16,boxShadow:'12px 12px 0 rgba(3,22,26,.38)',width:'80%',overflow:'hidden'}}>
  <div style={{background:`linear-gradient(90deg,${C.titleA},${C.blue})`,color:'#fff',font:'600 32px IBM Plex Sans',padding:'10px 18px',borderBottom:`4px solid ${C.edge}`}}>{title}</div>
  <div style={{padding:40,font:'500 40px IBM Plex Sans',color:C.edge,textAlign:'center'}}>{children}</div></div>;};
const Counter:React.FC<{n:Num}>=({n})=>{const f=useCurrentFrame();const dec=n.decimals??(String(n.value).split('.')[1]||'').length;
 const shown=n.status!=='VERIFIED'||n.value===null?'⚠ data needed':typeof n.value==='number'?(interpolate(f,[0,45],[0,n.value],{extrapolateRight:'clamp'})).toFixed(dec)+(n.unit||''):n.value+(n.unit||'');
 return <div style={{font:'700 160px "Pixelify Sans"',color:C.edge}}>{shown}</div>;};
export const PaperVideo:React.FC<Paper>=(p)=>{const by=Object.fromEntries(p.numbers.map(n=>[n.id,n]));const per=150;
 return <AbsoluteFill style={{background:`linear-gradient(180deg,${C.deskA},${C.deskB})`,alignItems:'center',justifyContent:'center'}}>
  <Sequence durationInFrames={120}><AbsoluteFill style={{alignItems:'center',justifyContent:'center'}}><Win title={`${p.citation.short_name??''}.paper`}><div style={{font:'700 72px "Pixelify Sans"'}}>{p.citation.short_name}</div>{p.citation.title}</Win></AbsoluteFill></Sequence>
  {p.hero_findings.map((h,i)=>(<Sequence key={h.number_id} from={120+i*per} durationInFrames={per}><AbsoluteFill style={{alignItems:'center',justifyContent:'center'}}><Win title={`finding_${i+1}.exe`}><Counter n={by[h.number_id]}/><div>{h.headline}</div></Win></AbsoluteFill></Sequence>))}
  <Sequence from={120+p.hero_findings.length*per} durationInFrames={150}><AbsoluteFill style={{alignItems:'center',justifyContent:'center'}}><Win title="what_changed.txt">{p.sections.practice_impact}<div style={{fontSize:28,marginTop:20}}>{p.citation.journal} {p.citation.year}</div></Win></AbsoluteFill></Sequence>
 </AbsoluteFill>;};
// Root.tsx: <Composition id="PaperVideo" component={PaperVideo} fps={30} width={1920} height={1080} durationInFrames={120+hero.length*150+150} defaultProps={paperJson}/>
// Add bar/forest scenes the same way: bar height = interpolate(frame,[0,40],[0,value]).
