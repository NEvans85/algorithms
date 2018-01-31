# prompt: https://www.hackerrank.com/challenges/two-characters/problem

"""
This algorithm checks if one can delete all instances of some twoCharacters
from a string to produce a string of two alternating characters and returns
the length of the longest such string.
It works by iterating through a list of the unique characters in the string,
picking each combination of two characters and testing if the string with
only those two characters satisfies the rule. If it does and it is longer than
the current best length, the best length is overwritten.
"""
import sys

def twoCharacters(s):
    uniqChars = list(set(list(s)))
    bestLenT = 0
    for i in range(len(uniqChars) - 1):
        for j in range(i+1, len(uniqChars)):
            delChars = uniqChars[:]
            delChars.pop(j)
            delChars.pop(i)
            testS = [ch for ch in s if ch not in delChars]
            if len(testS) > bestLenT and isT(testS):
                bestLenT = len(testS)
    return bestLenT

def isT(s):
    for idx in range(len(s) - 2):
        if s[idx] != s[idx + 2]:
            return False
    return True

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharacters(s)
    print(result)
