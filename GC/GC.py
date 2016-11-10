# coding: utf-8
# Potapov 4115
# this is my first code in python I prefer R 

with open('input.txt') as f:
    lines = f.readlines()

indexes = []
output = []
max_GC = 0.0
max_index = 0

# function for computing gc content of given DNA string
def GC(s):
    GC_content = 100.0 * (s.count("G") + s.count("C")) / len(s) 
    return GC_content

# first selecting indexes of dna definitions
for index, line in  enumerate(lines):
    if '>' in line:
        indexes.append(index)

indexes.append(len(lines))

# then producing an output
for n, index in enumerate(indexes[:-1]):
    output.append(lines[index][1:].replace('\n', ''))
    gc = GC("".join(lines[index+1:indexes[n+1]]).replace('\n', ''))
    # determining if we need to update max values
    if (gc > max_GC):
        max_GC = gc
        max_index = len(output)        
    output.append(str(gc))

# print output
# print output[max_index-1:max_index+1]
high_gc = output[max_index-1:max_index+1]

# writing output to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(high_gc))

