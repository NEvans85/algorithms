# prompt: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

import sys

def solve(arr, money):
    costIdxDict = {}
    for idx, amt in enumerate(arr):
        if money - amt in costIdxDict:
            print(costIdxDict[money - amt] + 1, idx + 1)
            return
        else:
            costIdxDict[amt] = idx


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
