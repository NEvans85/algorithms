# prompt: https://www.hackerrank.com/challenges/pangrams/problem

def pangram(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for ch in alphabet:
        if ch not in s:
            return False
    return True

s = input().lower()
if pangram(s):
    print('pangram')
else:
    print('not pangram')
