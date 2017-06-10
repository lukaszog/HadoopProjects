#!/usr/bin/env python
import sys
import re
import collections
from ast import literal_eval as make_tuple

lM = []
lL = []
suma = {}
for line in sys.stdin.readlines():
    for l in line.split("\n"):
        digit = re.search('[0-9]', l)
        if digit is not None:
            for i, k, m, j, v in [l.rstrip('\n').split(",")]:
                if m[3] == 'M':
                    lM.append(((i[2], k[1]), (m[3], int(j), int(v[:-3]))))
                elif m[3] == 'L':
                    lL.append(((i[2], k[1]), (m[3], int(j), int(v[:-3]))))

lM = sorted(lM, key=lambda tup: tup[1][1])
lL = sorted(lL, key=lambda tup: tup[1][1])

for eltM in lM:
    for eltL in lL:
        if (eltM[0] == eltL[0] and eltM[1][1] == eltL[1][1]):
            key = str(eltM[0][0]) + "," + str(eltL[0][1])
            if key not in suma:
                suma[key] = int(eltM[1][2]) * int(eltL[1][2])
            else:
                suma[key] += int(eltM[1][2]) * int(eltL[1][2])

for i in sorted(suma):
    print str(i) + "\t" + str(suma[i])
