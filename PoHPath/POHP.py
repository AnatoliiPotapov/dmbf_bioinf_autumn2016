# coding: utf-8
# Potapov 4115


# coding: utf-8

import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

in_str = lines[0].replace("\n","")
tr_prob = [lines[5].replace("\n","").split("\t")[1:3], lines[6].replace("\n","").split("\t")[1:3]]
# tr_prob = [float(el) for el in tr_prob]

class MM(object):
    
    alph = {}
    tr_matrix = []
    
    def __init__(self, alphabet, tr_prob):
        self.alph = alphabet
        self.tr_matrix = np.array(tr_prob).astype(np.float)

    def compute_transition_probability(self, ch1, ch2):
        return self.tr_matrix[self.alph[ch1], self.alph[ch2]]

        
ProbDistr = MM({'A':0, 'B':1}, tr_prob)
ProbDistr.compute_transition_probability('A','B')

index = 1
res_prob = 0.500
while index < len(in_str):
    res_prob *= ProbDistr.compute_transition_probability(in_str[index-1], in_str[index])
    index += 1

# writing output to file
with open('output.txt', 'w') as f:
    f.write(''.join(str(res_prob)))

