

# Naive implementation. Runs in O(n^2)
import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    resultList = [0 for _ in range(n)]
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a) - 1, int(b), int(k)]
        for idx in range(a, b):
            resultList[idx] += k
    print (max(resultList))
    
# Optimized impleentation. Runs in O(n)
# Uses a differential array rather than storing the actual values.
# Each value in this diff-array represents the difference between one element and the previous

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    diffList = [0 for _ in range(n + 1)]
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        diffList[a - 1] += k
        diffList[b] -= k
    total = 0
    maximum = 0
    for el in diffList:
        total += el
        if total > maximum:
            maximum = total
    print (maximum)