#!/usr/bin/python

import random;
import sys;

n = int(sys.argv[1]);
m = int(sys.argv[2]);

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sys.stdout.write("%d " % (random.randint(0, 100)));
    print "";
