#!/usr/bin/env python
import sys
import re

matrix = []
vec = {}
vector = False

for line in sys.stdin.readlines():
    digit = re.search('[0-9]', line)
    if digit is not None and len(line) > 5:
        for i, j, m in [line.rstrip('\n').split(";")]:
            matrix.append((int(i), int(j), int(m)))
    else:
        if digit is not None and not line == "\n":
            for j, m in [line.split(";")]:
                vec[int(j)] = int(m)
for l in matrix:
    print str(l[0]) + "\t" + str(l[2] * vec[l[1]])
