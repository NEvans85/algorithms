# prompt: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import defaultdict

def number_needed(a, b):
    count = 0
    chDict = defaultdict(int)
    for ch in a:
        chDict[ch] += 1
    for ch in b:
        chDict[ch] -= 1
    for ch in chDict:
        count += abs(chDict[ch])
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
