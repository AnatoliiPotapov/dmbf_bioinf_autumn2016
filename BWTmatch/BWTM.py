# coding: utf-8
# Potapov Anatoly 4115
# ### Пойск в строке при помощи преобразования BW и индексов FM

with open('input.txt') as f:
    lines = f.readlines()

# initializing string and substring
instr = lines[0].replace('\n', '')
patterns = lines[1].replace('\n', '').split(' ')

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

FMfunc = FM(instr)   

def LToF(FM, L, index):
    return FM.queryC(L[index]) + FM.queryOcc(L[index],index) - 1

def Match(L, p, top, bottom):
    first = -1
    last = -1
    for i in range(top, bottom+1):
        if L[i] == p:
            if (first == -1):
                first = i
                last = i
            else:
                last = i
    return [first, last]
                            
def BTW_matching(L, pattern, FM):
    top = 0
    bottom = len(L)-1
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            match = Match(L, symbol, top, bottom)
            if match[0] != -1:
                topIndex, bottomIndex = match
                top = LToF(FM, L, topIndex)
                bottom = LToF(FM, L, bottomIndex)
            else:
                return 0
        else:
            return bottom - top + 1

occurences = []
for pattern in patterns:
    occurences.append(BTW_matching(instr, pattern, FMfunc))

# writing output to file
with open('output.txt', 'w') as f:
    f.write(' '.join(str(x) for x in occurences))
