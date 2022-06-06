#combination in python

from itertools import combinations

numList=[1,2,3]
length = 2

comb = combinations(numList, length)

for i in comb:
    print(i)