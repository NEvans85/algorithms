# prompt: https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import math

def mean(numList):
    count = len(numList)
    total = 0
    for num in numList:
        total += num
    return total / float(count)

def stdDev(numList):
    listMean = mean(numList)
    totalSqDiff = 0
    for num in numList:
        totalSqDiff += (num - listMean) ** 2
    meanSqDiff = totalSqDiff / len(numList)
    return math.sqrt(meanSqDiff)

n = int(input())
intList = [int(x) for x in raw_input().split(" ")]
inputStdDev = stdDev(intList)
print (round(inputStdDev, 1))
