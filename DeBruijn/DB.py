# coding: utf-8
# Potapov 4115

import numpy as np
import copy

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]
# print lines

# Используется тривиальный алгоритм конструкции графа

class DB_graph(object):
    nodes = {}
    k_len = 0
    
    # Инициализируем граф ДеБрейна
    def __init__(self, strings):
        
        self.k_len = len(strings[0])-1
        
        for string in strings:
            
            prefix = string[:-1]
            suffix = string[1:]
        
            # инициализируем ноды
            self.nodes[prefix] = []
            self.nodes[suffix] = []
            
        # инициализируем вершины
        for node1 in self.nodes:
            for node2 in  self.nodes:
                if node1[1:] == node2[:-1]:
                    if not (node2 in self.nodes[node1]):
                        self.nodes[node1].append(node2)
                        
    def trace(self):       
        result = ''
        
        stack = []
        nodes = copy.deepcopy(self.nodes)
        
        v = ''
        for node in self.nodes:
            if len(self.nodes[node]) % 2 == 1:
                v = node
                break
        
        stack.append(v)
        
        while len(stack) > 0:
            
            w = stack[-1]
            
            for node in self.nodes[w]:
                stack.append(node)
                self.nodes[w].remove(node)
        
            if w == stack[-1]:
                # print w
                stack.pop()
                if (result == ''):
                    result = w
                else:
                    result = w[1] + result
                
        return result[:-self.k_len]
            
B = DB_graph(lines)
#print B.nodes
output = B.trace()

# writing output to file
with open('output.txt', 'w') as f:
    f.write(output)




