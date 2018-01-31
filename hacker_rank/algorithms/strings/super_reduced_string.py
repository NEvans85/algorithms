# prompt: https://www.hackerrank.com/challenges/reduced-string/problem

import sys

def super_reduced_string(s):
    newS = ''
    idx = 0
    while idx < len(s):
        if idx == len(s) - 1 or s[idx] != s[idx + 1]:
            newS += s[idx]
            idx += 1
        else:
            idx += 2
    if newS == s:
        return newS
    elif len(newS) == 0:
        return("Empty String")
    else:
        return super_reduced_string(newS)

s = input().strip()
result = super_reduced_string(s)
print(result)
