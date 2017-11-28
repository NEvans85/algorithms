# prompt: https://www.hackerrank.com/challenges/arrays-ds/problem

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for idx in range(len(arr) // 2):
    arr[idx], arr[len(arr) - idx - 1] = arr[len(arr) - idx - 1], arr[idx]

print (" ".join([str(x) for x in arr]))