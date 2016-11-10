# coding: utf-8
# Potapov 4115
# may not be optimal, but the question is will it work?

with open('input.txt') as f:
    lines = f.readlines()

# initializing string and substring
string = lines[0].replace('\n', '')
substr = lines[1].replace('\n', '')

# print str
# print substr

sub_length = len(substr)
main_str = substr + "#" + string
# print main_str

# function for calclulating Z-function O(n)
def z_function(s):
    
    n = len(s)
    z = [0 for j in range(n)]
    l, r = 0, 0
    
    for i in range(n):
        
        if (i <= r):
            z[i] = min(r-i+1, z[i-l])
            
        while (i+z[i] < n and s[z[i]] == s[i+z[i]]):
            z[i] = z[i] + 1
        
        if (i+z[i]-1 > r):
            l = i
            r = i+z[i]-1

    return z    

# calculating all occurencies of desired substring
z = z_function(main_str)
indices = [str(i - sub_length) for i, x in enumerate(z) if x == sub_length] 
# print indices

# writing output to file
with open('output.txt', 'w') as f:
    f.write(' '.join(indices))

