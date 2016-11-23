# coding: utf-8
# Potapov 4115
# may not be optimal, but the question is will it work?

with open('input.txt') as f:
    lines = f.readlines()

# initializing string 
str = lines[0].replace('\n', '')

# trivial Burrows-Wheeler transform
bwt = ''.join([i[-1] for i in sorted([str[i:] + str[0:i] for i in xrange(len(str))])])

# writing output to file
with open('output.txt', 'w') as f:
    f.write(bwt)

