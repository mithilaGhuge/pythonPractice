#take a command line argument to perform the list operation 
#such as insert element, remove the element from the list
#append the element to the list
#print the list 
from operator import ne
from re import I


if __name__ == '__main__':
    N = int(input())
    newList = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'insert':
            index = int(command[1])
            print(index)
            print(command[2])
            newList.insert(index, int (command[2]))
        elif command[0] == 'remove':
            newList.remove(int(command[1]))
        elif command[0] == 'append':
            newList.append(command[1])
        elif command[0] == 'sort':
            for i in newList:
                if type(i) != int:
                    newList.remove(i)
                    newList.append(int(i))
            print(newList)
            newList.sort()
        elif command[0] == 'reverse':
            newList.reverse()
            print(newList)
        elif command[0] == 'print':
            print(newList)
        elif command[0] == 'pop':
            newList.pop()
        


