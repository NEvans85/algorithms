# prompt: https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = int(input())
vals = [int(x) for x in raw_input().split(" ")]
weights = [int(x) for x in raw_input().split(" ")]
weightedTotal = 0
totalWeight = 0
for idx in range(n):
    weightedTotal += vals[idx] * weights[idx]
    totalWeight += weights[idx]
weightedMean = weightedTotal / float(totalWeight)
print (round(weightedMean, 1))
