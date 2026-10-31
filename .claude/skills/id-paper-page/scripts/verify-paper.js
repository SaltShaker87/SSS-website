// Step 3 gate: every number appears in its source_quote and every figure references real numbers.
// Usage: node verify-paper.js papers/<slug>/paper.json
const path=require('path');
const p=require(path.resolve(process.argv[2]||'paper.json'));
const WORDS=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty'];
const quoted=(value,quote)=>{
 const q=quote.replace(/,/g,'').replace(/[−–]/g,'-'),v=String(value).replace(/,/g,'');
 // Whole numbers only: 1 matches 1.0 but not 13.2 or 1.5. JSON drops trailing zeros, so 0.4 matches 0.40.
 const digits=new RegExp('(?<![\\d.])'+v.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+(v.includes('.')?'0*':'(?:\\.0+)?')+'(?!\\d|\\.\\d)');
 const word=WORDS[Number(v)];
 return digits.test(q)||(!!word&&new RegExp('\\b'+word+'\\b','i').test(q));
};
let bad=0;
for(const n of p.numbers){
 if(n.value===null){console.log('MISSING',n.id);bad++;continue}
 if(n.derived&&n.formula)continue; // Step 3.2: shown with its formula, not quoted
 if(!quoted(n.value,n.source_quote)){console.log('UNVERIFIED',n.id,n.value);bad++}
}
for(const f of p.figures)for(const r of f.number_ids)if(!p.numbers.find(n=>n.id===r)){console.log('BAD REF',f.id,r);bad++}
console.log(bad?'FAIL '+bad:'PASS');
process.exitCode=bad?1:0;
