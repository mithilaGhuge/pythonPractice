#binary search 
#in binary search elements in the list should be sorted
# you need to find upper bond and lower bond of the list 
#need to find the mid value

arrList = [2,5,7,4,68,99,45,67,8,3]
elemToFind = 45
arrList.sort()

pos = -1

def binarySearch(arrList,elemToFind):
    lowerBound = 0
    upperBound = len(arrList)-1
    found = False
    while lowerBound <= upperBound:
        mid = (lowerBound + upperBound) // 2

        if arrList[mid] == elemToFind:
            found = True
            globals()['pos'] = mid
            break
        elif arrList[mid] > elemToFind:
            upperBound = mid-1
        elif arrList[mid] < elemToFind:
            lowerBound = mid+1
        else:
            found = False

    if found:
        print("element found in list at",pos)
    else:
        print("element not found in list at")

binarySearch(arrList,elemToFind)