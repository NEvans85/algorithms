# prompt: https://www.hackerrank.com/challenges/ctci-coin-change/problem

import sys

def make_change(coins, n):
    sCoins = sorted(coins)
    dpMatrix = [[] for idx in range(n+1)]
    for rIdx, row in enumerate(dpMatrix):
        if rIdx == 0:
            for _ in sCoins:
                row.append(1)
        else:
            for cIdx, coin in enumerate(sCoins):
                if cIdx == 0:
                    row.append(1 if rIdx % coin == 0 else 0)
                elif rIdx - coin < 0:
                    row.append(row[-1])
                else:
                    row.append(row[-1] + dpMatrix[rIdx-coin][cIdx])
    return dpMatrix[-1][-1]



n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
