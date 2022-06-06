#permutation and combination in python
#First import itertools package to implement the permutations method 
#in python. This method takes a list as an input and returns 
#an object list of tuples that contain all permutations in a list form. 

from itertools import permutations
# sample code for permutations
# numList = [1,1,3]
# permutationList = permutations(numList)

# for i in permutationList:
#     print(i)

# hackerrank code for permutations where string is given 

inString = "HACK"
lengthS = 2
strList=[]
permList = permutations(inString,lengthS)
for com in permList:
    strNew =''
    for i in com:
        strNew+=i
    strList.append(strNew)

for i in sorted(strList):
    print(i)