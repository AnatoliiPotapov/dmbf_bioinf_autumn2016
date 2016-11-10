# coding: utf-8
# Potapov 4115
# may be not optimal, but the question is will it work?

with open('input.txt') as f:
    lines = f.readlines()

str = lines[0]
kmer_len = int(lines[1])
# print string
# print kmer_len

# creating a dictionary for kmer number of occurencies
kmers = {}
common_kmers = []

# going through all substringth of length kmer_len
for index in range(len(str) - kmer_len):
    kmer = str[index:(index + kmer_len)]
    # if kmer is already present in dictionary
    if kmer in kmers:
        kmers[kmer] = kmers[kmer] + 1
    else:
        kmers[kmer] = 1

# sorting a dictionary
sorted_kmers = sorted(kmers.items(), key=lambda x: -x[1])

# getting only the most common kmers
most_common_num = sorted_kmers[0][1]

for kmer in sorted_kmers:
    if (kmer[1] == most_common_num):
        common_kmers.append(kmer[0])

# print(common_kmers)

# writing output to file
with open('output.txt', 'w') as f:
    f.write(' '.join(common_kmers))

