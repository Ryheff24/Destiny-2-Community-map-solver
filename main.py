import json
from enum import nonmember

import numpy as np

# Load the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
dict = {}
for i in range(1, 4097, 1):
    dict[i] = []

# print(dict)
# Loop through each top-level key and get the "fen" value
zero = []
one = []
bunch = []
dict2 = {}
master = {}
# print(len(data))
for key, value in data.items():
    fen_value = value.get('fen')
    seq = value.get('sequence')
    if int(seq) > 4096 or int(seq) < 1:
        continue
    if len(fen_value.split('/')) != 8:
        print(fen_value)
    if fen_value == "///////" or len(fen_value.split('/')) != 8:
        continue
    dict[seq].append((key, value))
    # print(f"{seq}: {fen_value}")
with open('dump.json', 'r') as f:
    data2 = json.load(f)
def getseq(seq, data2):
    for k, v in data2.items():
        # print(k, v)
        if seq ==  v.get('sequence'):
            return k, v
        else:
            continue
    return None, None
for key, value in dict.items():
    # print(len(value))
    if len(value) == 0:
        zero.append(value)
        continue
    if len(value) == 1:
        # print(value)
        # one.append(data.get(value[0][0]))
        master[value[0][0]] = value[0][1]
        continue
    if len(value) >= 2:
        # print(value[1][1])
        k,v = getseq(value[1][1].get('sequence'), data2)
        if k is None or v is None: print("this is none")
        master[k] = v
        continue
print(len(master.keys()))
with open('output.json', 'w') as f:
    json.dump(master.items(), f)