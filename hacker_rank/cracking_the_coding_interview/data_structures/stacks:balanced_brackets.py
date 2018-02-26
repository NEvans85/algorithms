# prompt: https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def is_matched(expression):
    stack = []
    brackets = {'(':')', '{':'}', '[':']'}
    for ch in expression:
        if ch in {'(','[','{'}:
            stack.append(ch)
        elif len(stack) == 0:
            return False
        else:
            match = stack.pop()
            if brackets[match] != ch:
                return False
    return len(stack) == 0


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
