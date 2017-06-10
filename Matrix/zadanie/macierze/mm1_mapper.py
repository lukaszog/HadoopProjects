#!/usr/bin/env python
import sys
import re

mac = []
for line in sys.stdin.readlines():
    digit = re.search('[0-9]', line)
    if digit is not None:
        if 'M' in line:
            x = 0
        elif 'L' in line:
            x = 1
        for m, i, j, v in [line.rstrip('\n').split(";")]:
            if x==0:
                mac.append((int(j), (m, int(i), int(v))))
            elif x==1:
                mac.append((int(i), (m, int(j), int(v))))
mac.sort()
for l in mac:
    print str(l[0]) + "\t" + str(l[1])
