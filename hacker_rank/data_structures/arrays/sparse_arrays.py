# prompt: 

n = int(input())
countDict = {}
for _ in range(n):
    iStr = input()
    if iStr in countDict:
        countDict[iStr] += 1
    else:
        countDict[iStr] = 1
q = int(input())
for _ in range(q):
    qStr = input()
    if  qStr in countDict:
        print (countDict[qStr])
    else:
        print (0)