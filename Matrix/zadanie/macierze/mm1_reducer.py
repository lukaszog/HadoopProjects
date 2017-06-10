#!/usr/bin/env python
import sys
import re
from ast import literal_eval as make_tuple

lstM = []
lstL = []
for line in sys.stdin.readlines():
    for l in line.split("\n"):
        digit = re.search('[0-9]', l)
        if digit is not None:
            for j, v in [l.rstrip('\n').split("\t")]:
                v = make_tuple(v)
                if 'M' in v:
                    lstM.append((int(j),v))
                elif 'L' in v:
                    lstL.append((int(j),v))

lstM=sorted(lstM, key=lambda tup: tup[0]) 
lstM=sorted(lstM, key=lambda tup: tup[1][1]) 
lstL=sorted(lstL, key=lambda tup: tup[0]) 

for eltM in lstM:
    for eltL in lstL:
        if(eltM[0]==eltL[0]):
            print str(eltM[1][1]) + "," + str(eltL[1][1]) + "\t" + str(int(eltM[1][2])*int(eltL[1][2]))
