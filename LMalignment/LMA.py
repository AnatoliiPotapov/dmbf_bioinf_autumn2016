# coding: utf-8

# Python is so slow!!!!!!!
# Потратили много времени, зато научились вызывать С код

# uahahah we are going with numpy this time
import numpy as np
import blosum
from scipy import weave

amino_acids = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
al = len(amino_acids)
amino_dict = {a: n for n,a in enumerate(amino_acids)}

blosum = blosum.Matrix("blosum62.txt")

penalty = np.zeros((len(amino_acids), len(amino_acids)), dtype=np.int)

for i in range(len(amino_acids)):
    for j in range(len(amino_acids)):
        penalty[i,j] = int(blosum.lookup_score(amino_acids[i],amino_acids[j]))

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
# converting sequenses into numpy arrays
ns1 = np.array([amino_dict[s] for s in seq1])
ns2 = np.array([amino_dict[s] for s in seq2])

# initializing edit matrix
m = np.zeros((len(ns1)+1, len(ns2)+1), dtype=np.int)
l = np.zeros((len(ns1)+1, len(ns2)+1), dtype=np.int)
r = np.zeros((len(ns1)+1, len(ns2)+1), dtype=np.int)

# initializing path matrix
path = np.zeros((len(ns1)+1, len(ns2)+1))
path[:,0] = [0 for i in range(len(ns1)+1)]
path[0,:] = [0 for i in range(len(ns2)+1)] 

l1 = len(ns1)
l2 = len(ns2)

code = """
    
    #define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; })
     
    int i, j;
    int pos, posD, posR, posU;
    int h = l2+1;
    int diag;
    
    for (i=1; i< l1+1; i++) {    
        for (j=1; j< l2+1; j++) {  
            
            pos  = (i)*h + (j);
            posD = (i-1)*h + (j-1); 
            posR = (i)*h + (j-1); 
            posU = (i-1)*h + (j);
            
            m[pos] = 0;
            path[pos] = 0;

            l[pos] = max(l[posU] - 1, m[posU] - 11);
            r[pos] = max(r[posR] - 1, m[posR] - 11);
            diag = m[posD]+penalty[ns1[i-1]*al+ns2[j-1]];
            
            m[pos] = max(max(l[pos],r[pos]), max(diag,0));
            
            if (m[pos]==l[pos]) path[pos]=2;
            if (m[pos]==r[pos]) path[pos]=3;
            if (m[pos]==diag) path[pos]=1;
            
        }
    }
"""
res = weave.inline(code, ['m','l','r','path','l1','l2','al','ns1','ns2','penalty'], compiler = 'gcc')

output.append(str(int(m.max())))
(x_max, y_max) = np.where(m == m.max())
# print (x_max, y_max)
# print m

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

# print seq1[i:x_max[0]]
# print seq2[j:y_max[0]]

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))
