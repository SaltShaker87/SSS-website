// Deterministic hero video. Every number comes from the props (built from paper.json); nothing is hardcoded.
import React from 'react';
import {AbsoluteFill, Sequence, cancelRender, continueRender, delayRender, interpolate, spring, useCurrentFrame, useVideoConfig, Easing} from 'remotion';

const fonts = delayRender('site fonts');
const css = document.createElement('link');
css.rel = 'stylesheet';
css.href = 'https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@700&family=IBM+Plex+Sans:wght@500;600&display=block';
css.onload = () => Promise.all(['700 16px "Pixelify Sans"', '500 16px "IBM Plex Sans"', '600 16px "IBM Plex Sans"'].map((f) => document.fonts.load(f))).then(() => continueRender(fonts)).catch(cancelRender);
css.onerror = () => cancelRender(new Error('Could not load site fonts'));
document.head.appendChild(css);

type Bar = {label: string; value: number | null; unit: string; decimals?: number | null; role: string};
type Finding = {value: number | string | null; unit: string; decimals?: number | null; status: string; headline: string; bars: Bar[] | null};
export type Props = {
  citation: {title: string; short_name: string; journal: string; year: number};
  topic: string;
  who: {big: string; label: string; design: string};
  findings: Finding[];
  outro: string;
  timing: {title: number; who: number; finding: number; outro: number};
  frames: number;
};

const C = {deskA: '#117178', deskB: '#0a4650', face: '#eef0f3', paper: '#ffffff', edge: '#141a24', ink2: '#39414f', salt: '#ffd23f', blue: '#1f82e0', titleA: '#0b1f8f', muted: '#586173'};

const dec = (v: number, d?: number | null) => (d ?? (String(v).split('.')[1] || '').length);
const show = (v: number, d: number) => {
  const s = Math.abs(v).toFixed(d);
  return (v < 0 && Number(s) !== 0 ? '−' : '') + s;
};

const Desk: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: `radial-gradient(circle at 18% 12%, rgba(255,210,63,.18), transparent 40%), radial-gradient(circle at 85% 90%, rgba(31,130,224,.22), transparent 45%), linear-gradient(180deg, ${C.deskA}, ${C.deskB})`, alignItems: 'center', justifyContent: 'center'}}>
    <AbsoluteFill style={{backgroundImage: 'radial-gradient(rgba(255,255,255,.06) 1px, transparent 1px)', backgroundSize: '8px 8px'}} />
    {children}
  </AbsoluteFill>
);

const Win: React.FC<{title: string; width?: string; dur: number; children: React.ReactNode}> = ({title, width = '78%', dur, children}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 13, mass: 0.8}});
  const out = interpolate(f, [dur - 10, dur], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <div style={{transform: `scale(${s * (0.94 + 0.06 * out)})`, opacity: out, background: C.face, border: `4px solid ${C.edge}`, borderRadius: 18, boxShadow: '14px 14px 0 rgba(3,22,26,.38), 0 40px 80px -20px rgba(0,0,0,.45)', width, overflow: 'hidden'}}>
      <div style={{display: 'flex', alignItems: 'center', gap: 14, background: `linear-gradient(90deg, ${C.titleA}, ${C.blue})`, color: '#fff', font: '600 30px "IBM Plex Sans"', padding: '12px 20px', borderBottom: `4px solid ${C.edge}`}}>
        <div style={{width: 22, height: 22, background: C.salt, border: `3px solid ${C.edge}`}} />
        <div style={{flex: 1}}>{title}</div>
        {[0, 1, 2].map((i) => <div key={i} style={{width: 30, height: 26, background: C.face, border: `3px solid ${C.edge}`, borderRadius: 5}} />)}
      </div>
      <div style={{padding: '44px 56px', font: '500 40px/1.3 "IBM Plex Sans"', color: C.edge, textAlign: 'center'}}>{children}</div>
    </div>
  );
};

const Counter: React.FC<{n: Finding; size?: number}> = ({n, size = 168}) => {
  const f = useCurrentFrame();
  if (n.status !== 'VERIFIED' || n.value === null) return <div style={{font: `700 ${size * 0.5}px "Pixelify Sans"`, color: '#b91c1c'}}>⚠ data needed</div>;
  if (typeof n.value !== 'number') return <div style={{font: `700 ${size}px "Pixelify Sans"`}}>{n.value + n.unit}</div>;
  const d = dec(n.value, n.decimals);
  const k = interpolate(f, [8, 50], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
  const v = n.value * k;
  return <div style={{font: `700 ${size}px/1.05 "Pixelify Sans"`, color: C.edge, letterSpacing: 2}}>{show(v, d)}{n.unit}</div>;
};

const Bars: React.FC<{bars: Bar[]}> = ({bars}) => {
  const f = useCurrentFrame();
  const vals = bars.map((b) => (typeof b.value === 'number' ? Math.abs(b.value) : 0));
  const max = Math.max(...vals, 1e-9);
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap: 16, marginTop: 30, textAlign: 'left'}}>
      {bars.map((b, i) => {
        const k = interpolate(f, [30 + i * 10, 80 + i * 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
        const w = (vals[i] / max) * 100 * k;
        const col = b.role === 'comparator' ? C.blue : b.role === 'neutral' ? C.muted : C.salt;
        return (
          <div key={i} style={{display: 'flex', alignItems: 'center', gap: 20}}>
            <div style={{width: 330, font: '600 32px "IBM Plex Sans"', color: C.ink2, textAlign: 'right'}}>{b.label}</div>
            <div style={{flex: 1, height: 54, background: C.paper, border: `3px solid ${C.edge}`, borderRadius: 8, overflow: 'hidden'}}>
              <div style={{width: `${w}%`, height: '100%', background: col, borderRight: w > 0 ? `3px solid ${C.edge}` : 'none'}} />
            </div>
            <div style={{width: 230, font: '700 44px "Pixelify Sans"', opacity: k}}>{typeof b.value === 'number' ? show(b.value, dec(b.value, b.decimals)) + b.unit : '⚠'}</div>
          </div>
        );
      })}
    </div>
  );
};

const Tag: React.FC<{text: string}> = ({text}) => (
  <span style={{display: 'inline-block', font: '600 28px "IBM Plex Sans"', background: C.salt, border: `3px solid ${C.edge}`, borderRadius: 99, padding: '2px 18px', marginBottom: 18}}>{text}</span>
);

export const PaperVideo: React.FC<Props> = (p) => {
  const T = p.timing;
  const name = p.citation.short_name;
  let t = 0;
  const seq = (dur: number, node: React.ReactNode, key: string) => {
    const from = t;
    t += dur;
    return <Sequence key={key} from={from} durationInFrames={dur}><Desk>{node}</Desk></Sequence>;
  };
  return (
    <AbsoluteFill style={{background: C.deskB}}>
      {seq(T.title, <Win title={`${name.toLowerCase().replace(/[^a-z0-9]+/g, '-')}.paper`} dur={T.title}><Tag text={p.topic} /><div style={{font: '700 96px/1.05 "Pixelify Sans"', marginBottom: 22}}>{name}</div><div style={{font: '500 38px/1.3 "IBM Plex Sans"', color: C.ink2}}>{p.citation.title}</div><div style={{font: '600 30px "IBM Plex Sans"', color: C.muted, marginTop: 24}}>{p.citation.journal} · {p.citation.year}</div></Win>, 'title')}
      {seq(T.who, <Win title="who_was_studied.txt" dur={T.who}><div style={{font: '700 150px/1.05 "Pixelify Sans"'}}>{p.who.big}</div><div style={{marginTop: 12}}>{p.who.label}</div><div style={{font: '600 30px "IBM Plex Sans"', color: C.muted, marginTop: 22}}>{p.who.design}</div></Win>, 'who')}
      {p.findings.map((h, i) => seq(T.finding, <Win title={`finding_${i + 1}.exe`} dur={T.finding}><Counter n={h} size={h.bars ? 140 : 168} /><div style={{marginTop: 14}}>{h.headline}</div>{h.bars ? <Bars bars={h.bars} /> : null}</Win>, `f${i}`))}
      {seq(T.outro, <Win title="what_changed.txt" dur={T.outro + 20}><div style={{font: '700 56px "Pixelify Sans"', marginBottom: 20}}>What changed</div>{p.outro}<div style={{font: '600 30px "IBM Plex Sans"', color: C.muted, marginTop: 26}}>{name} · {p.citation.journal} {p.citation.year} · Educational summary, not medical advice</div></Win>, 'outro')}
    </AbsoluteFill>
  );
};
