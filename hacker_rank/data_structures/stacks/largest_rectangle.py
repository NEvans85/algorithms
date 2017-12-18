# prompt: https://www.hackerrank.com/challenges/largest-rectangle/problem

import sys

def largestRectangle(h):
    posStack = [0]
    hStack = [h[0]]
    maxSize = 0
    idx = 1
    while idx < len(h):
        if len(hStack) == 0 or h[idx] > hStack[-1]:
            posStack.append(idx)
            hStack.append(h[idx])
        elif h[idx] < hStack[-1]:
            while len(hStack) > 0 and h[idx] < hStack[-1]:
                tempPos = posStack.pop()
                maxSize = max([maxSize, hStack.pop() * (idx - tempPos)])
            hStack.append(h[idx])
            posStack.append(tempPos)
        idx += 1
    while len(hStack) > 0:
        maxSize = max([maxSize, hStack.pop() * (idx - posStack.pop())])
    return maxSize

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
