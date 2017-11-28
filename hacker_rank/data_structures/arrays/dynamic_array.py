# prompt: https://www.hackerrank.com/challenges/dynamic-array/problem

n, q = [int(x) for x in input().split(" ")]
seqList = [[] for _ in range(n)]
lastAnswer = 0
for _ in range(q):
    t, x, y = [int(x) for x in input().split(" ")]
    idx = (x ^ lastAnswer) % n
    if t == 1:
        seqList[idx].append(y)
    else:
        lastAnswer = seqList[idx][y % len(seqList[idx])]
        print (lastAnswer)