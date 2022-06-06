import operator
import re


if __name__ == '__main__':
    nameList = []
    scorelist = []
    reqName = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameList.append(name)
        scorelist.append(score)

studentDict = {}
for i in range(0,len(nameList)):
    studentDict[nameList[i]] = scorelist[i]

final_list = sorted(studentDict.items(), key=operator.itemgetter(1))
result = dict([(k,v) for k, v in final_list])

for i in range(len(studentDict)-1,0,-1):
    for j in range(i):
        if 


    
        
