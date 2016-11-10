# coding: utf-8
# Potapov 4115
# may not be optimal, but the question is will it work?

# import some useful shit
import numpy
import lcs

with open('input.txt') as f:
    lines = f.readlines()

dna_string = lines[0].rstrip('\n')
# print dna_string

# We will be constructing generalized suffix tree with Uchonen algoithm
tree = lcs.SuffixTree()
tree.append_string(dna_string, manual_ending = True)
map_string = ''.join(tree.input_string)

# Инициализируем вывод
output = []

# Пройдемся по дереву до листьев и соберем все бананы
edges = tree.root.edges

def get_edges(edges):
    for edge in edges.items():
        current_node = edge[1]
        output.append(map_string[current_node.start : current_node.end])
        get_edges(current_node.edges)
        
get_edges(edges)
# print output

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(output))



