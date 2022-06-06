#selection sort using python
#swap only selected value in the list

from re import A
from tkinter import N


arrList = [12,3,56,78,2,56,1]
newList = arrList
print("new list",newList)
def sort(arrList):
    for i in range(0,len(arrList)-1):
        minPos = i
        for j in range(i,len(arrList)):
            if arrList[j] < arrList[minPos]:
                minPos = j
            
                
        temp = arrList[i] 
        arrList[i] = arrList[minPos]
        arrList[minPos] = temp
        


    return arrList
print(sort(arrList))