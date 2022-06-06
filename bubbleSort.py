#Bubble sort using python

arrList=[12,45,6,2,89,1,24]

def sort(arrList):
    for i in range(len(arrList)-1,0,-1):
        for j in range(i):
            if arrList[j]>arrList[j+1]:
                temp = arrList[j]
                arrList[j] = arrList[j+1]
                arrList[j+1] = temp
    
    return arrList
print(sort(arrList))


