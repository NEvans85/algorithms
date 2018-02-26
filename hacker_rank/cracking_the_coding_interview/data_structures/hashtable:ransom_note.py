# prompt: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

from collections import defaultdict

def ransom_note(magazine, ransom):
    wordCount = defaultdict(int)
    for word in magazine:
        wordCount[word] += 1
    for word in ransom:
        if word not in wordCount or wordCount[word] == 0:
            return False
        else:
            wordCount[word] -= 1
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
