# coding: utf-8
# Potapov Anatoly 4115

with open('input.txt') as f:
    lines = f.readlines()

# initializing string and substring
in_str = lines[0].replace('\n', '')
index = int(lines[1])

# naive implementation of FM functions
class FM(object):
    freq = {}
    alphabet = []
    C = {}
    Occ = []
    def __init__(self, str):
        
        # Custom comparison
        comp = {'$':0, 'A':1, 'C':2, 'G':3, 'T':4}
        # Calculationg alphabet(sorted)
        alphabet = sorted(comp, key= lambda x: comp[x])
        zero_dict = {}
        # Init frequences
        for key in comp:
            self.freq[key] = 0
            zero_dict[key] = 0 
        
        # Calculating frequences
        for ch in str:
            if ch in self.freq:
                self.freq[ch] += 1
            else:
                self.freq[ch] = 1
        
        # Calculating C function
        counter = 0
        for key in alphabet:
            self.C[key] = counter
            counter+= self.freq[key]
            
        # Calculating Occ
        new_dict = zero_dict
        last_dict = zero_dict
        for i in range(len(str)):
            ch = str[i]
            new_dict[ch] = last_dict[ch] + 1
            self.Occ.append(new_dict.copy())
            last_dict = new_dict
            

    def queryC(self, ch):
        return self.C[ch]
    
    def queryOcc(self, ch, ind):
        return self.Occ[ind][ch]        

FMfunc = FM(in_str)
result = FMfunc.queryC(in_str[index]) + FMfunc.queryOcc(in_str[index],index) - 1

# writing output to file
with open('output.txt', 'w') as f:
    f.write(str(result))
