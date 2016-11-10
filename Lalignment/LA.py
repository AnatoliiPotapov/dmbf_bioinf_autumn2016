# coding: utf-8
# Potapov 4115

# uahahah we are going with numpy this time
import numpy as np
import blosum

# exploring class which provides interface to blossum matrix
pam = blosum.Matrix("PAM250.txt")
# pam.lookup_score("A", "A")

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

# print seq1
# print seq2

# initializing edit matrix

m = np.zeros((len(seq1)+1, len(seq2)+1))
m[:,0] = [-5*i for i in range(len(seq1)+1)]
m[0,:] = [-5*i for i in range(len(seq2)+1)] 

# initializing path matrix

path = np.zeros((len(seq1)+1, len(seq2)+1))
path[:,0] = [0 for i in range(len(seq1)+1)]
path[0,:] = [0 for i in range(len(seq2)+1)] 

# then calculating an edit matrix 
for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        
        # let the magic begin!
        m[i, j] = 0
        path[i, j] = 0
        
        # 1 - diagonal
        # 2 - right
        # 3 - down
        
        if m[i, j] < m[i-1, j-1] + int(pam.lookup_score(seq1[i-1], seq2[j-1])):
            m[i, j] = m[i-1, j-1] + int(pam.lookup_score(seq1[i-1], seq2[j-1]))
            path[i, j] = 1
            
        if m[i, j] < m[i-1, j] - 5:
            m[i, j] = m[i-1, j] - 5
            path[i, j] = 2
            
        if m[i, j] < m[i, j-1] - 5:
            m[i, j] = m[i, j-1] - 5
            path[i, j] = 3

output.append(str(int(m.max())))
(x_max, y_max) = np.where(m == m.max())
# print (x_max, y_max)

# going back collecting alignment

alignment = []
i = x_max[0]
j = y_max[0]

while not (path[i,j] == 0):
    
    if path[i,j] == 1:
        alignment.append((i,j))
        if i>0: i-=1
        if j>0: j-=1
        
    if path[i,j] == 3:
        alignment.append((i,j))
        if j>0: j-=1
    
    if path[i,j] == 2:
        alignment.append((i,j))
        if i>0: i-=1

alignment.append((i,j))
# print alignment

# producing output
output.append(seq1[i:x_max[0]])
output.append(seq2[j:y_max[0]])

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))

