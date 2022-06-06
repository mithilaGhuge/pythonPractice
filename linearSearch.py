#linear search from list 

from turtle import clear


arrList = [1,6,5,8,3,9,4]
elemToFind = 9
pos = -1

def search(arrList, elemToFind):
    found = False
    for  index, value in enumerate(arrList):
        if value == elemToFind: 
            found = True
            globals()['pos'] = index
            break
        else:
            found = False
    
    if found == True:
        print("element is present in list at", pos+1)
    else:
        print("element is not present in list")

search(arrList,elemToFind)