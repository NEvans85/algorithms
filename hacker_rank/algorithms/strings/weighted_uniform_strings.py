# prompt: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

"""
This algorithm stores possible weights in a set to allow for constant time
checks for inclusion.
"""

import sys
s = input().strip()
n = int(input().strip())
scores = set([])
chCount = 1
for idx, ch in enumerate(s):
    scores.add((ord(ch) - 96) * chCount)
    if idx + 1 < len(s) and s[idx + 1] == ch:
        chCount += 1
    else:
        chCount = 1
for a0 in range(n):
    x = int(input().strip())
    if x in scores:
        print('Yes')
    else:
        print('No')
