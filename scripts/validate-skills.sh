#!/bin/sh
set -eu
seen=""
for d in skills/*; do [ -d "$d" ] || continue; f="$d/SKILL.md"; test -f "$f" || { echo "missing $f"; exit 1; }; n=$(basename "$d"); grep -q "^name: $n$" "$f" || { echo "bad name $n"; exit 1; }; grep -q '^description:' "$f" || { echo "missing description $n"; exit 1; }; case " $seen " in *" $n "*) exit 1;; esac; seen="$seen $n"; done
for n in page-inventory information-architecture user-flow design-system-reader page-layout-designer design-validator figma-screen-builder frontend-context-reader figma-to-frontend frontend-design-validator; do grep -q "name: $n" registry/creation-log.yaml || exit 1; done
echo PASS
