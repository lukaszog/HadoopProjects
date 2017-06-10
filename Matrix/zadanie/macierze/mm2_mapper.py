#!/usr/bin/env python
import sys
import re

mac = []
for line in sys.stdin.readlines():
    digit = re.search('[0-9]', line)
    if digit is not None:
        print line.rstrip('\n')
