#!/usr/bin/env python
import sys
import re
import collections
from ast import literal_eval as make_tuple

lst = []
dct = {}
for line in sys.stdin.readlines():
    for l in line.split("\n"):
        digit = re.search('[0-9]', l)
        if digit is not None:
            for j, v in [l.rstrip('\n').split("\t")]:
                if j not in dct:
                    dct[j] = int(v)
                else:
                    dct[j] += int(v)

for i in sorted(dct):
    print str(i) + "\t" + str(dct[i])

