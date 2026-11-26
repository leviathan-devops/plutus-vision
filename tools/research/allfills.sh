#!/bin/bash
# usage: allfills.sh TAG  -> fills of the 16 maps into scratchpad/fills_TAG.txt + a one-line tally (bug locator only)
SP=/tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad
cd /home/user/plutus-vision
: > $SP/fills_$1.txt
for m in $(cat /home/user/plutus-vision/tools/research/maps16.txt); do python3 tools/research/fills.py ${m%%:*} ${m##*:} 2>&1 | grep -v "^LOG\|^  log" >> $SP/fills_$1.txt; done
echo "TP $(grep -o 'TP HIT' $SP/fills_$1.txt | wc -l) STOPPED $(grep -o 'STOPPED' $SP/fills_$1.txt | wc -l) setups $(grep -c ' E [0-9]' $SP/fills_$1.txt)"
