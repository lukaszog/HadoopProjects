#!/usr/bin/env python
import sys
import re
import collections

dct = {}

for line in sys.stdin.readlines():
    for l in line.split("\n"):
        digit = re.search('[0-9]', l)
        if digit is not None:
            for j, v in [l.split("\t")]:
                if j not in dct:
                    dct[j] = int(v)
                else:
                    dct[j] += int(v)
for elt in range(len(dct)):
    print str(elt) + "\t" + str(dct[str(elt)])
