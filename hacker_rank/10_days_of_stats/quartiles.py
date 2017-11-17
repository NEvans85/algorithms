# prompt: https://www.hackerrank.com/challenges/s10-quartiles/problem

def median(numList):
    count = len(numList)
    if count % 2 == 0:
        return ((numList[count / 2] + numList[(count / 2) - 1]) / 2.0)
    else:
        return (numList[count / 2])

def quartiles(numList):
    count = len(numList)
    Q1 = median(numList[0:(count / 2)])
    Q2 = median(numList)
    if count % 2 == 0:
        Q3 = median(numList[(count / 2):count])
    else:
        Q3 = median(numList[((count / 2) + 1):count])
    print (int(Q1))
    print (int(Q2))
    print (int(Q3))

n = int(input())
intList = sorted([int(x) for x in raw_input().split(" ")])
quartiles(intList)
