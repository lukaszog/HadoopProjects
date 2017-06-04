#!/usr/local/bin/python3
import fileinput
import json

JOIN_COLUMN_INDEX = {
    'Orders': 1,
    'Customers': 0
}

for line in fileinput.input():
    if line and line.strip():
        words = line.split("\t")

        table_name = words[0]
        data = words[1:]

        join_column_index = JOIN_COLUMN_INDEX[table_name]
        map_key = data[join_column_index]
        map_value = json.dumps((table_name, data[0:join_column_index] + data[join_column_index + 1:]))

        # print("table name %s, value %s " % (table_name, value))
        print("%s\t%s" % (map_key, map_value))

