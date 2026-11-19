import React from 'react';
import {Composition} from 'remotion';
import {PaperVideo, Props} from './PaperVideo';

const empty: Props = {
  citation: {title: 'Title', short_name: 'PAPER', journal: 'Journal', year: 2020},
  topic: 'Topic', who: {big: '0', label: '', design: ''}, findings: [], outro: '',
  timing: {title: 120, who: 165, finding: 180, outro: 180}, frames: 465,
};

export const Root: React.FC = () => (
  <Composition
    id="PaperVideo"
    component={PaperVideo as unknown as React.FC<Record<string, unknown>>}
    fps={30}
    width={1920}
    height={1080}
    durationInFrames={465}
    defaultProps={empty as unknown as Record<string, unknown>}
    calculateMetadata={({props}) => ({durationInFrames: (props as unknown as Props).frames})}
  />
);
