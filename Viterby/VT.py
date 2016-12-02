# coding: utf-8
# Potapov 4115

import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.replace("\t", " ").replace("\n", "") for line in lines]
# print lines

# parsing data

l_obs = lines[0]
obs_alph = lines[2].split(" ")
hid_alph = lines[4].split(" ")

# print obs_alph

alph_obs = {}
for ind,el in enumerate(obs_alph):
    if el!="":
        alph_obs[el] = ind


alph_hid = {}
for ind,el in enumerate(hid_alph):
    if el!="":
        alph_hid[el] = ind 

def read_matrix(lines, start, n, last = False):
    m = []
    for i in range(n):
        if last == True and i == n-1:
            m.append(lines[start + i].replace("\n","").split(" ")[1:])
        else:
            m.append(lines[start + i].replace("\n","").split(" ")[1:-1])
    return m

tr_prob = read_matrix(lines, 7, len(alph_hid))
tr_emission = read_matrix(lines, 7 + 2 + len(alph_hid), len(alph_hid), last = True)

print tr_prob, tr_emission

# инициализируем скрытую марковскую модель

class HMM(object):
    
    alph_hidden = {}
    alph_viz = {}
    
    tr_m = []
    em_m = []
    
    def __init__(self, alph_hidden, alph_viz, tr_prob, tr_emission):
        
        self.alph_hidden = alph_hidden
        self.alph_viz = alph_viz
        
        self.tr_m = np.array(tr_prob).astype(np.float)
        self.em_m = np.array(tr_emission).astype(np.float)
    
    # для пары скрытых состояний возвращает вероятность шифта
    def get_tr_p(self, ch1, ch2):
        return self.tr_m[ch1, ch2]
    
    # для данного скрытого и видимого состояния возвращает вероятность эмиссии
    def get_em_p(self, hid, viz):
        return self.em_m[hid, self.alph_viz[viz]]
    
Hmm = HMM(alph_hid, alph_obs, tr_prob, tr_emission)

print Hmm.alph_hidden
print Hmm.alph_viz

# Viterbi algorithm implementation

def get_path(Hmm, in_str):
    
    # t - длина входной строки
    t = len(in_str)
    # k - размер алфавита наблюдаемых состояний
    k = len(Hmm.alph_viz)
    # h - размер алфавита скрытых состояний
    h = len(Hmm.alph_hidden)
    
    # score - максимум произведения весов по всем путям из начала до данной вершины
    score = np.zeros((h,t))
    # index - путь, соответствующий наибольшему score
    index = np.zeros((h,t))
    
    # # # # # #
    score[:,0] = 1 * np.array([Hmm.get_em_p(st,in_str[0]) for st in range(h)])
    
    for i in range(t)[1:]:
        for st in range(h):
            pre_sc = [score[ind, i-1] + np.log(Hmm.get_tr_p(st,ind)) + np.log(Hmm.get_em_p(st,in_str[i])) for ind in range(h)]
            pre_sc_i = [score[ind, i-1] + np.log(Hmm.get_tr_p(st,ind)) for ind in range(h)]

            score[st, i] = np.max(pre_sc)
            index[st, i] = np.argmax(pre_sc_i)
    
    
    # print score
    # print index
    
    # обратный ход алгоритма
    v_path = np.zeros(t)
    v_path[t-1] = np.argmax(score[:,t-1])
    
    for i in range(t)[1:][::-1]:
        v_path[i - 1] = index[v_path[i], i]

    rev_d = dict(zip(Hmm.alph_hidden.values(),Hmm.alph_hidden.keys()))    
    
    # print [rev_d[state] for state in v_path]
    return [rev_d[state] for state in v_path]

output = get_path(Hmm, l_obs)

# writing output to file
with open('output.txt', 'w') as f:
    f.write(''.join(output)+"\n")


