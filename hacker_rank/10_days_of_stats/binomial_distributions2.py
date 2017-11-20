# prompt: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial (num - 1)

def binDist(n, x, p):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))

inputs = [int(x) for x in raw_input().split(" ")]
prob = inputs[0] / 100.0
probs = [binDist(inputs[1], x, prob) for x in range(inputs[1] + 1)]
print round(sum(probs[0:3]), 3)
print round(sum(probs[2:(inputs[1] + 1)]),3)
