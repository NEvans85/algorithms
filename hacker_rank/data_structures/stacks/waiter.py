# prompt: https://www.hackerrank.com/challenges/waiter/problem

import sys
import math

def firstNPrimes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num == 1:
        return False
    sq = int(math.sqrt(num))
    for i in range(3, sq +1, 2):
        if num % i == 0:
            return False
    return True

n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
aStack = list(map(int, input().strip().split(' ')))
bStacks = []
primes = firstNPrimes(q)
for i in range(q):
    newAStack = []
    bStacks.append([])
    while len(aStack) > 0:
        el = aStack.pop()
        if el % primes[i] == 0:
            bStacks[i].append(el)
        else:
            newAStack.append(el)
    aStack = [x for x in newAStack]
for s in bStacks:
    while len(s) > 0:
        print (s.pop())
while len(aStack) > 0:
    print(aStack.pop())
