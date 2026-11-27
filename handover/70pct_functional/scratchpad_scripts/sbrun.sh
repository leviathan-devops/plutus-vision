#!/bin/bash
# usage: sbrun.sh TAG [sync]  -> sandbox ($SP/sb) fills + per-leg locator + golden diff vs the repo baseline (od_d99_*). 'sync' first copies the repo's e1_tool + tools/research into the sandbox.
SP=/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad
if [ "$2" = sync ]; then rsync -a --delete --exclude __pycache__ /home/user/plutus-vision/e1_tool/ $SP/sb/e1_tool/; rsync -a --exclude __pycache__ /home/user/plutus-vision/tools/research/ $SP/sb/tools/research/; echo synced; exit 0; fi
cd $SP/sb
: > $SP/fills_$1.txt; : > $SP/legs_$1.txt
for m in $(tr " " "\n" < tools/research/maps16.txt); do python3 tools/research/fills.py ${m%%:*} ${m##*:} 2>&1 | grep -v "^LOG\|^  log" >> $SP/fills_$1.txt; done
echo "TP $(grep -o 'TP HIT' $SP/fills_$1.txt | wc -l) STOPPED $(grep -o 'STOPPED' $SP/fills_$1.txt | wc -l) setups $(grep -c ' E [0-9]' $SP/fills_$1.txt)"
for m in $(tr " " "\n" < tools/research/maps16.txt | grep -v 2026-07-06 | grep -v "DXY:2026-04-20"); do python3 tools/research/legs.py ${m%%:*} ${m##*:} $SP/fills_$1.txt >> $SP/legs_$1.txt 2>&1; done
grep LOCATOR $SP/legs_$1.txt | awk '{split($2,a,"/"); c+=a[1]; n+=a[2]} END {print "legs caught " c "/" n}'
grep "legs$\|LOCATOR" $SP/legs_$1.txt | paste - - | awk '{print $1, $2, $NF}' | tr "\n" ";"; echo
for p in DXY EURUSD GBPUSD; do python3 tools/research/oracle_diff.py $p > $SP/od_$1_$p.txt 2>&1; diff -q $SP/od_$1_$p.txt $SP/od_d99_$p.txt >/dev/null && echo "$p golden unchanged" || echo "$p golden CHANGED"; done
