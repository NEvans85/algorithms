# prompt: https://www.hackerrank.com/challenges/balanced-brackets/problem

import sys

def isBalanced(s):
    bStack = []
    for ch in s:
        if ch in ['(', '{', '[']:
            bStack.append(ch)
        else:
            if len(bStack) == 0:
                return 'NO'
            lastOpener = bStack.pop()
            if ch == ')' and lastOpener != '(':
                return 'NO'
            if ch == ']' and lastOpener != '[':
                return 'NO'
            if ch == '}' and lastOpener != '{':
                return 'NO'
    if len(bStack) == 0:
        return 'YES'
    else:
        return 'NO'




if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
