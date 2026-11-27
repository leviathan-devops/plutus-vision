#!/bin/bash
# usage: alllegs.sh TAG [sandbox-dir] -> per-leg locator (tools/research/legs.py) over the non-anchor maps of maps16.txt, from scratchpad/fills_TAG.txt (run allfills.sh TAG first). BUG LOCATOR ONLY.
SP=/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad
cd /home/user/plutus-vision
: > $SP/legs_$1.txt
for m in $(tr " " "\n" < tools/research/maps16.txt | grep -v 2026-07-06 | grep -v "DXY:2026-04-20"); do python3 tools/research/legs.py ${m%%:*} ${m##*:} $SP/fills_$1.txt >> $SP/legs_$1.txt 2>&1; done
grep LOCATOR $SP/legs_$1.txt | awk '{split($2,a,"/"); c+=a[1]; n+=a[2]} END {print "legs caught " c "/" n}'
grep "legs$\|LOCATOR" $SP/legs_$1.txt | paste - - | awk '{print $1, $2, $NF}' | tr "\n" ";"; echo
