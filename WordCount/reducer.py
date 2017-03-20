#!/usr/bin/python
import fileinput

last = None
count = 0
for line in fileinput.input():
    word = line.split()[0]
    if last != word:
        if last:
            print("%s\t%d" % (last, count))

        last = word
        count = 1
    else:
        count += 1


