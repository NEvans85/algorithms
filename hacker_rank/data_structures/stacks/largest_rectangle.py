# prompt: https://www.hackerrank.com/challenges/largest-rectangle/problem

import sys

def largestRectangle(h):
    posStack = [0]
    hStack = [h[0]]
    maxSize = 0
    for idx in range(1, len(h)):
        if h[idx] > h[posStack[-1]]:
            posStack.append(idx)
            hStack.append(h[idx])
        elif h[idx] < h[posStack[-1]]:
            maxSize = max([maxSize, hStack.pop() * (idx - positions[-1])])
            hStack.append(h[idx])
    return maxSize

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
