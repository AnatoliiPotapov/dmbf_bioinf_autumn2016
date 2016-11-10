# coding: utf-8
# Potapov 4115
# may not be optimal, but the question is will it work?

# import some useful shit
import numpy
import lcs

with open('input.txt') as f:
    lines = f.readlines()

indexes = []
strings = []
prefixes = []

# first selecting indexes of dna definitions
for index, line in  enumerate(lines):
    if '>' in line:
        indexes.append(index)
        
indexes.append(len(lines))
n = len(indexes)

cur_length = 0

# populting strings list
for n, index in enumerate(indexes[:-1]):
    sequence = "".join(lines[index+1:indexes[n+1]]).replace('\n', '')    
    strings.append(sequence)

# We will be constructing generalized suffix tree with Uchonen algoithm
tree = lcs.SuffixTree()

for string in strings:
    tree.append_string(string)
    
longest_substrings = tree.find_longest_common_substrings()

# writing output to file
with open('output.txt', 'w') as f:
    f.write(''.join(longest_substrings[0]))

