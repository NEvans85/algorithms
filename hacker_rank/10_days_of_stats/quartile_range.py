# prompt: https://www.hackerrank.com/challenges/s10-interquartile-range/problem

def median(numList):
    count = len(numList)
    if count % 2 == 0:
        return ((numList[count / 2] + numList[(count / 2) - 1]) / 2.0)
    else:
        return float(numList[count / 2])

def quartileRange(numList):
    count = len(numList)
    Q1 = median(numList[0:(count / 2)])
    if count % 2 == 0:
        Q3 = median(numList[(count / 2):count])
    else:
        Q3 = median(numList[((count / 2) + 1):count])
    return (Q3 - Q1)

n = int(input())
vals = [int(x) for x in raw_input().split(" ")]
freq = [int(x) for x in raw_input().split(" ")]
data = []
for idx in range(n):
    for _ in range(freq[idx]):
        data.append(vals[idx])
sortedData = sorted(data)
print (quartileRange(sortedData))
