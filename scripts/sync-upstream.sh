#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
UPSTREAM="$ROOT/.tmp/upstream"
mkdir -p "$UPSTREAM"

sync_repo() {
  name=$1
  url=$2
  dir="$UPSTREAM/$name"
  if [ -d "$dir/.git" ]; then
    git -C "$dir" fetch --depth 1 origin
    git -C "$dir" reset --hard origin/HEAD
  else
    git clone --depth 1 "$url" "$dir"
  fi
  git -C "$dir" rev-parse HEAD
}

matt=$(sync_repo mattpocock-skills https://github.com/mattpocock/skills.git)
super=$(sync_repo superpowers https://github.com/obra/superpowers.git)

python3 - "$ROOT/UPSTREAM.lock.json" "$matt" "$super" <<'PY'
import json, sys
from pathlib import Path
p=Path(sys.argv[1]); data=json.loads(p.read_text())
commits={'mattpocock/skills':sys.argv[2], 'obra/superpowers':sys.argv[3]}
for item in data:
    if item['repository'] in commits: item['commit']=commits[item['repository']]
p.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
PY
printf '%s\n' "Upstreams synchronized and UPSTREAM.lock.json updated."
