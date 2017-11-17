# prompt: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import math

def isPrime(num):
    if num == 2:
        return "Prime"
    if num % 2 == 0 or num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for i in range(3, sq +1, 2):
        if num % i == 0:
            return "Not prime"
    return "Prime"

n = int(input())
for _ in range(n):
    toTest = int(input())
    print(isPrime(toTest))
