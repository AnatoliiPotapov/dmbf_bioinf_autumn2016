# coding: utf-8
# Potapov 4115

# uahahah we are going with numpy this time
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

indexes = []
output = []

# first selecting indexes of dna definitions
for index, line in  enumerate(lines):
    if '>' in line:
        indexes.append(index)

indexes.append(len(lines))

# print indexes

# populating sequences
seq1 = "".join(lines[indexes[0]+1:indexes[1]]).replace('\n', '')
seq2 = "".join(lines[indexes[1]+1:indexes[2]]).replace('\n', '')

# seq1 = "sunny"
# seq2 = "snowy"

# print seq1
# print seq2

# initializing edit matrix
m = np.zeros((len(seq1)+1, len(seq2)+1))
m[:,0] = range(len(seq1)+1)
m[0,:] = range(len(seq2)+1)

# print m

# D[i, j] ← min(
#    D[i − 1, j] + 1,
#    D[i, j − 1] + 1,
#    D[i − 1, j − 1] + (V [i] 6= W[j])
# )

# then calculating an edit matrix 
for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        m[i, j] = min(
        m[i-1, j] + 1,
        m[i, j-1] + 1,
        m[i-1, j-1] + (seq1[i-1] != seq2[j-1])
        )

# print m

# producing output
output.append(str(int(m[len(seq1), len(seq2)])))

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

