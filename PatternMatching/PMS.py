# coding: utf-8
# Potapov Anatoly 4115

# Пока что будем решать на тривиальном алгоритме суффиксного массива

# import some useful shit
import numpy
from bisect import bisect_left, bisect_right

with open('input.txt') as f:
    lines = f.readlines()

dna_string = lines[0].rstrip('\n')
patterns = [line.rstrip('\n') for line in lines[1:]]
#print dna_string
#print patterns

# Инициализируем вывод
output = []

# Самый наивный алгоритм
def construct_suffix_array(t):
    suffixes = sorted([(i, t[i:]) for i in xrange(len(t))], key = lambda item: item[1])
    return suffixes 

def next_p(pattern):
    l = ['A','C','G','T','X']
    ch = pattern[len(pattern)-1] 
    new_ch = l[[i for i in range(len(l)) if l[i] == ch][0]+1]
    new_pattern = pattern[:-1]
    new_pattern+= new_ch
    return new_pattern

def find_all_occurencies(suff_arr, pattern):
    suff_sorted = [item[1] for item in suff_arr]
    indexes_sorted = [item[0] for item in suff_arr]
    st, en = bisect_left(suff_sorted, pattern), bisect_left(suff_sorted, next_p(pattern))
    return indexes_sorted[st:en]

suffix_array = construct_suffix_array(dna_string)

for pattern in patterns:
    output.extend(find_all_occurencies(suffix_array, pattern))

# print output

# writing output to file
with open('output.txt', 'w') as f:
    f.write(' '.join([str(el) for el in output]))

