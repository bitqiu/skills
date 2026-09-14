#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
DEST=${SKILLS_HOME:-${HOME}/.codex/skills/product-engineering}
if [ "${FORCE:-0}" != "1" ] && [ -e "$DEST" ]; then
  echo "目标目录已存在：$DEST（使用 FORCE=1 覆盖）" >&2
  exit 1
fi
"$ROOT/scripts/validate-skills.sh"
mkdir -p "$DEST"
for skill in "$ROOT"/skills/*; do
  [ -d "$skill" ] || continue
  name=$(basename "$skill")
  rm -rf "$DEST/$name"
  cp -R "$skill" "$DEST/$name"
done
echo "已安装到 $DEST"
