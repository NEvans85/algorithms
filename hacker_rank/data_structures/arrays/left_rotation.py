# prompt: https://www.hackerrank.com/challenges/array-left-rotation/problem

import sys

def leftRotation(a, d):
    lst = a
    for _ in range(d):
        lst.append(lst.pop(0))
    return lst

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))

