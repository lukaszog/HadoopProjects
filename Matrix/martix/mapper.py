import fileinput
import json


for line in fileinput.input():
    data = line.strip().split(';')

    label = data[0]
    i = int(data[1])
    j = int(data[2])
    m_ij = int(data[3])

    d = dict()
    if label == "M":
        d[j] = (label, i, m_ij)  # m[i][j] z pdf
    else:
        d[i] = (label, j, m_ij)  # l[j][k] z pdf

    print(json.dumps(d))
