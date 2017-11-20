# prompt: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial (num - 1)

def binDist(n, x, p):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))

ratio = [float(x) for x in raw_input().split(" ")]
probB = (ratio[0]) / (ratio[0] + ratio[1])
threeBoys = binDist(6, 3, probB)
fourBoys = binDist(6, 4, probB)
fiveBoys = binDist(6, 5, probB)
sixBoys = binDist(6, 6, probB)
totalProb = threeBoys + fourBoys + fiveBoys + sixBoys
print round(totalProb, 3)
