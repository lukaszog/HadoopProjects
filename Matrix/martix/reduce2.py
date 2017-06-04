import json
import fileinput

sum_for_key = 0
previous_key = None
i = None
k = None

for line in fileinput.input():
    d = json.loads(line.strip())
    # print(d)
    key = list(d.keys())[0]
    value = d[key]

    curr_key = json.loads(key)

    if previous_key != curr_key:
        if previous_key is not None:
            print("%d;%d;%d" % (previous_key[0], previous_key[1], sum_for_key))
        previous_key = curr_key
        sum_for_key = value
    else:
        sum_for_key += value


print("%d;%d;%d" % (previous_key[0], previous_key[1], sum_for_key))