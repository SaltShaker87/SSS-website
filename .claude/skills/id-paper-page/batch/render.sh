#!/bin/bash
# Usage: bash render.sh slug [slug...]
SITE="/c/Users/yalci/OneDrive/Documents/SSS logos and files and stuff/Website test 1"
cd "$(dirname "$0")"
for s in "$@"; do
  P=../build/out/$s.props.json
  npx remotion render src/index.ts PaperVideo "out/$s.mp4" --props=$P --codec=h264 --crf=28 --concurrency=6 --log=error && \
  npx remotion still src/index.ts PaperVideo "out/$s.jpg" --props=$P --frame=60 --image-format=jpeg --jpeg-quality=80 --log=error && \
  cp "out/$s.mp4" "$SITE/papers/$s/video.mp4" && cp "out/$s.jpg" "$SITE/papers/$s/poster.jpg" && echo "RENDERED $s $(du -h out/$s.mp4 | cut -f1)" || echo "FAILED $s"
done
