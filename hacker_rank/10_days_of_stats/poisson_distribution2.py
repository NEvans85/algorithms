# prompt: https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

avgs = [float(x) for x in raw_input().split(" ")]
avgA = avgs[0]
avgB = avgs[1]

print round((160 + 40 * (avgA ** 2 + avgA)), 3)
print round((128 + 40 * (avgB ** 2 + avgB)), 3)
