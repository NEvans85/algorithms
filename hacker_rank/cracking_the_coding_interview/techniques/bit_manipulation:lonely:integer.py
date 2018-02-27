# prompt: https://www.hackerrank.com/challenges/ctci-lonely-integer/problem

import sys

def lonely_integer(a):
    value = 0
    for i in a:
        value ^= i
    return value

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
