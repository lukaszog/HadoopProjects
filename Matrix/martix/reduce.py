import fileinput
import json


list_for_j = []
current_j = None


def compute_list_for_j(grouped_list):
    from_m = [a for a in grouped_list if a[0] == 'M']
    from_l = [a for a in grouped_list if a[0] == 'L']
    # print("m", from_m)
    # print("l", from_l)
    for m in from_m:
        for l in from_l:
            ret = dict()
            ret[json.dumps((m[1], l[1]))] = m[2] * l[2]
            print(json.dumps(ret))


for line in fileinput.input():

    data = json.loads(line.strip())

    key = list(data.keys())[0]
    value = data[key]

    if current_j is None or current_j != key:

        if current_j:
            compute_list_for_j(list_for_j)

        current_j = key
        list_for_j = [value]

    else:
        list_for_j.append(value)

compute_list_for_j(list_for_j)