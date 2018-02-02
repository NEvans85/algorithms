# prompt:

"""
This algorithm counts the number of character deletions it would take to
change a string to a string of alternating characters. It works by counting
the number of repeating characters.
"""

import sys

def alternatingCharacters(s):
    repCh = 0
    idx = 0
    while idx < len(s):
        while idx < len(s) - 1 and s[idx] == s[idx + 1]:
            repCh += 1
            idx += 1
        idx += 1
    return repCh

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
