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

# populating sequences
seq1 = "".join(lines[indexes[0]+1:indexes[1]]).replace('\n', '')
seq2 = "".join(lines[indexes[1]+1:indexes[2]]).replace('\n', '')

# but that`s not all, we need to store traces, fuck`n traces!
# 0 - diagonal
# 1 - downside
# 2 - rightside

# initializing edit matrix
m = np.zeros((len(seq1)+1, len(seq2)+1))
m[:,0] = range(len(seq1)+1)
m[0,:] = range(len(seq2)+1)

# initializing trace matrix
tr = np.zeros((len(seq1)+1, len(seq2)+1))
tr[:,0] = [2] * (len(seq1)+1)
tr[0,:] = [1] * (len(seq2)+1)
tr[0, 0] = 0

# then calculating both
for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        
    
        m[i, j] = m[i-1, j-1] + (seq1[i-1] != seq2[j-1])
        tr[i, j] = 0
        
        if m[i, j] > m[i-1, j] + 1:
            m[i, j] = m[i-1, j] + 1
            tr[i, j] = 2
        
        if m[i, j] > m[i, j-1] + 1:
            m[i, j] = m[i, j-1] + 1
            tr[i, j] = 1

# producing output
output.append(str(int(m[len(seq1), len(seq2)])))

# going back collecting alignment
i = len(seq1)
j = len(seq2)

# Quick lambda function to insert indels.
insert_indel = lambda word, i: word[:i] + '-' + word[i:]

while (i*j != 0):

    if tr[i,j] == 0:
        i-=1
        j-=1
        
    if tr[i,j] == 1:
        seq1 = insert_indel(seq1, i)
        j-=1
    
    if tr[i,j] == 2:
        seq2 = insert_indel(seq2, j)
        i-=1

# Prepend the necessary preceeding indels to get to (0,0).
for repeat in range(i):
    seq2 = insert_indel(seq2, 0)
for repeat in range(j):
    seq1 = insert_indel(seq1, 0)

# producing outputs
output.append(seq1)
output.append(seq2)

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

