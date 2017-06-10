#!/usr/bin/env python
import sys
import re

mM = []
mL = []
mlL = []
mlM = []
for line in sys.stdin.readlines():
    digit = re.search('[0-9]', line)
    if digit is not None:
        if 'M' in line:
            x = 0
        elif 'L' in line:
            x = 1
        for m, i, j, v in [line.rstrip('\n').split(";")]:
            if x==0:
                mM.append((int(i), (m, int(j), int(v))))
            elif x==1:
                mL.append((int(j), (m, int(i), int(v))))

x = max(mM, key=lambda tup: tup[0])[0]
y = max(mM, key=lambda tup: tup[1][1])[1][1]
#tmp = []
for elt in mM:
    for k in range(y+1):
        print (((elt[0], k), ('M', elt[1][1], elt[1][2])))
    #mlM.append(tmp)
    #tmp = []
for elt in mL:
    for i in range(x+1):
        print (((i, elt[0]), ('L', elt[1][1], elt[1][2])))
   # mlL.append(tmp)
   # tmp = []


#mlM=sorted(mlM, key=lambda tup: tup[1][1])
#mlL=sorted(mlL, key=lambda tup: tup[1][1])

#for eltM in mlM:
#    for eltL in mlL:
#        print eltM[0][0], eltL[0][1]
#        if(eltM[0][0]==eltL[0][1]):
#            print str(eltM[1][1]) + "," + str(eltL[1][1]) + "\t" + str(int(eltM[1][2])*int(eltL    [1][2]))

