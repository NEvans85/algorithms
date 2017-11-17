# prompt: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

n = int(input())
rawStr = raw_input()
intList = [int(x) for x in rawStr.split(" ")]
sortedList = sorted(intList)
total = 0
countDict = {}
maxCount = 1
modeVals = []
for num in sortedList:
    total += num
    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1
    if countDict[num] > maxCount:
        maxCount = countDict[num]
        modeVals = [num]
    elif countDict[num] == maxCount:
        modeVals.append(num)
mean = total / float(n)
if n % 2 == 0:
    median = (sortedList[n / 2] + sortedList[(n / 2) - 1]) / 2.0
else:
    median = sortedList[n / 2]
print (mean)
print (median)
print (modeVals[0])
