# coding: utf-8
# Potapov 4115

import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

in_str_hidden = lines[0].replace("\n","")
in_alph = lines[2].replace("\n","").split("\t")
alph_hidden = {}

for ind,el in enumerate(in_alph):
    alph_hidden[el] = ind

in_str_viz = lines[4].replace("\n","")
in_alph = lines[6].replace("\n","").split("\t")
alph_viz = {}

for ind,el in enumerate(in_alph):
    alph_viz[el] = ind    
    
tr_prob = [lines[9].replace("\n","").split("\t")[1:4], lines[10].replace("\n","").split("\t")[1:4]]

class HMM(object):
    
    alph_hidden = {}
    alph_viz = {}
    tr_matrix = []
    
    def __init__(self, alph_hidden, alph_viz, tr_prob):
        self.alph_hidden = alph_hidden
        self.alph_viz= alph_viz
        self.tr_matrix = np.array(tr_prob).astype(np.float)

    def compute_transition_probability(self, ch1, ch2):
        return self.tr_matrix[self.alph_viz[ch1], self.alph_hidden[ch2]]

        
ProbDistr = HMM(alph_hidden, alph_viz, tr_prob)

index = 0
res_prob = 1.000
while index < len(in_str_viz):
    res_prob *= ProbDistr.compute_transition_probability(in_str_viz[index], in_str_hidden[index])
    index += 1

# writing output to file
with open('output.txt', 'w') as f:
    f.write(''.join(str(res_prob)))


