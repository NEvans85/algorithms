# prompt: https://www.hackerrank.com/challenges/separate-the-numbers/problem

"""
This algoritm checks if a string is a series of sequential integers.
I works by constructing a test string for each potential first integer
then checking if it equals the given string.
"""

import sys

def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    for idx in range(1, (len(s) // 2) + 1):
        testS = s[:idx]
        firstNum = testS[:]
        lastNum = int(firstNum)
        while len(testS) < len(s):
            nextNum = lastNum + 1
            testS += str(nextNum)
            lastNum = nextNum
            if testS != s[:len(testS)]:
                break
        if testS == s:
            print("YES " + firstNum)
            return
    print("NO")

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
