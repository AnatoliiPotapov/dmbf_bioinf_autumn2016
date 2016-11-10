# coding: utf-8
# Potapov 4115

with open('input.txt') as f:
    lines = f.readlines()

# reading parameters
[n, m] = lines[0].split()
n = int(n)
m = int(m)
# print n, m

# algorithm ** rabbit paradise **
ages = [0] * m
ages[0] = 1

for year in range(n-1): 
    
    # increase population
    new_rabbits = sum(ages[1:])
    
    # birthday party
    ages[1:] = ages[:-1]
    ages[0] = new_rabbits
    
    # update population
    population = sum(ages)

# print population

# writing output to file
with open('output.txt', 'w') as f:
    f.write(str(population))

