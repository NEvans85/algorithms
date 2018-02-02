
"""
This algorithm determines how many times a character must be reduced
(changed to the previous letter) in order to make the input string into
a palindrome. It works by adding the difference between the ascii values
of each char in the first half of the string with its mirrored counterpart
in the last half to a running total (diff).
"""

import sys

def theLoveLetterMystery(s):
    diff = 0
    for i in range(len(s) // 2):
        diff += abs(ord(s[i]) - ord(s[-1*(i+1)]))
    return diff

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
