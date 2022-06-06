#create a decorator for logging of stackTrace.py 
#decorators are used to change the behaviour of the function or class without\
#modifying the function signature

from operator import le


def wrapper(f):
    def fun(l):
        newList =[]
        # complete the function
        # def makePhoneNum(num,x):
        #     return  " ".join(["+91",num[x:x+5],num[x+5:]]) 
        
        #lambda function for makePhoneNum

        #makeNum = lambda num , x : " ".join(["+91",num[x:x+5],num[x+5:]])
        
        numLengthDict = {
                        10:lambda num : " ".join(["+91",num[0:5],num[5:]]),
                        11:lambda num : " ".join(["+91",num[1:6],num[6:]]),
                        12:lambda num : " ".join(["+91",num[2:7],num[7:]]),
                        13:lambda num : " ".join(["+91",num[3:8],num[8:]])
                        }
        for num in l:
            lenNum = len(num)
            newList.append(numLengthDict[lenNum](num))
        # 10 --> num[x:x+5] num[x+5:]
        # 11 --> num[1:6] num[6:]
        # 12 --> num[2:7] num[7:]
        # 13 --> num[3:8] num[8:]
        # for num in l :
        #     lengthNum = len(num)
        
        #     #case 1: 0
        #     if lengthNum == 11:
        #         newList.append(makePhoneNum(num[1:]))
        #     #case 2: 91
        #     elif lengthNum == 12:
        #         newList.append(makePhoneNum(num[2:]))
        #     #case 3: +91
        #     elif lengthNum == 13:
        #         newList.append(makePhoneNum(num[3:]))
        #     #case 4: none
        #     elif lengthNum==10:
        #         newList.append(makePhoneNum(num))
        
        f(newList)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
    