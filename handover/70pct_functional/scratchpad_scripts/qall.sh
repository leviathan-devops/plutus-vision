#!/bin/bash
# qall.sh DIR : qual.py over the 12 count maps in DIR (repo or sandbox) + totals
cd $1
for m in $(tr " " "\n" < tools/research/maps16.txt | head -12); do python3 tools/research/qual.py ${m%%:*} ${m##*:}; done | tee /tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad/q_last.txt | cut -c1-150
awk '{for(i=1;i<=NF;i++){if($i=="bloated")b+=$(i+1); if($i=="pairs")u+=$(i+1); if($i=="floating")f+=$(i+1); if($i=="missing"){split($(i+1),a,"/"); m+=a[1]} if($i=="zones")z+=$(i-1)}} END {print "TOTAL zones " z " bloated " b " bunched " u " floating " f " missing " m}' /tmp/claude-0/-home-user-plutus-vision/b6c77a81-471c-536b-9631-0319cefbf3ab/scratchpad/q_last.txt
