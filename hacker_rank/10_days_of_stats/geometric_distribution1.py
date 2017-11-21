# prompt: https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

def geoDist(i, p):
    return ((1 - p) ** (i - 1)) * p

oddsList = [int(x) for x in raw_input().split(" ")]
odds = float(oddsList[0]) / oddsList[1]
targetI = int(input())
print round(geoDist(targetI, odds), 3)
