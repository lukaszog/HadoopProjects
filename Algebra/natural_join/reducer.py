#!/usr/local/bin/python3
import fileinput
import json
from collections import defaultdict

groups = defaultdict(list)


def reduce_natural_join(key, list_of_relation_data):
    group_by_table = defaultdict(list)
    result_dict = {}
    for d in list_of_relation_data:
        group_by_table[d[0]].append(d[1])

    if len(group_by_table) == 2:
        keys = list(group_by_table.keys())
        for record in group_by_table[keys[0]]:
            for r2 in group_by_table[keys[1]]:
                row = record + [key] + r2
                print("%s\t%s" % (key, json.dumps(row)))

for line in fileinput.input():
    parts = line.split()
    relation_column_val = parts[0]
    relation_data = json.loads(' '.join(parts[1:]))
    groups[relation_column_val].append(relation_data)


for k in groups:
    reduce_natural_join(k, groups[k])