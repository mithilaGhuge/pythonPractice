
from re import L
from webbrowser import get


def findMax(arr):
    visitedIndex = []
    currentMax = 0
    while len(visitedIndex)< len(arr):
        currentIndex=getMaxIndex(visitedIndex, arr)
        previousMax = arr[currentIndex]
        tempMax = 0
        blockMax = 0
        for i in range(currentIndex,0,-1):
            tempMax = max(arr[i], previousMax-1)
            previousMax =tempMax
            blockMax += tempMax
        
        if blockMax<currentMax:
            currentMax = blockMax

        visitedIndex.append(currentIndex)

    return currentMax

def getMaxIndex(visitedIndex,arr):
    listProd =[]
    for i in arr:
        if arr[i] not in visitedIndex:
            listProd.append(arr[i])
    
    return max(listProd)
        
