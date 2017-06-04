import re;
import sys;

i = 1;
for line in sys.stdin:
    arr = re.split("[ \t]+", line.strip());
    j = 1;
    for v in arr:
        print("%d %d\t%s" % (i, j, v));
        j += 1;
    i += 1;
