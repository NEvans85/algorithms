# prompt: https://www.hackerrank.com/challenges/the-power-sum/problem

import sys

def powerSum(X, N, maxInt):
    count = 0
    for testInt in range(maxInt, 0, -1):
        if X - testInt ** N == 0:
            count += 1
        elif X - testInt ** N < 0:
            continue
        else:
            count += powerSum(X - testInt ** N, N, testInt - 1)
    return count

if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    maxInt = int(X**(1/N))
    result = powerSum(X, N, maxInt)
    print(result)
