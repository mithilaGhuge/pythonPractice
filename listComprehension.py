#list comprehension in python
#List comprehension offers a shorter syntax when you want to create 
# new list based on the values of an existing list.
# the syntax--> newlist = [expression for item in iterable if condition == True]
#create a list of numbers from 1 to 100
#and using list comprehension filter all multiples of 4

# numList = [i for i in range(1,101) if i%4==0]
# print(numList)

from itertools import permutations
if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
    
    # first tried solution
    # x = list(range(0,x+1))
    # y = list(range(0,y+1))
    # z = list(range(0,z+1))
    # finalList = []
    # for numX in x:
    #     for numY in y:
    #         for numZ in z:
    #             finalList.append((numX,numY,numZ))
    #outputList = [x for x in finalList if sum(x)!=n]

    # revised solution
    finalList = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c !=3]

    for i in finalList:
        print(i)

    
    # permutationsList = permutations()

    # for i in permutationsList:
    #     print(i)
