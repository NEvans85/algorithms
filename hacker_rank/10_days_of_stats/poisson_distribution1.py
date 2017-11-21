# prompt: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

def poissonDist(avg, act):
    return ((avg ** act) * (2.71828 ** (-1 *avg))) / factorial(act)

avg = float(input())
act = float(input())
print round(poissonDist(avg, act), 3)
