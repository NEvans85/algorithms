#prompt https://www.hackerrank.com/challenges/insertionsort1/problem

n = int(input())
rawList = input().split(" ")
intList = [int(x) for x in rawList]
toInsert = intList[len(intList) - 1]
idx = len(intList) - 2
while intList[idx] > toInsert and idx >= 0:
    intList[idx + 1] = intList[idx]
    idx -= 1
    print(" ".join([str(el) for el in intList]))
intList[idx + 1] = toInsert
print(" ".join([str(el) for el in intList]))
