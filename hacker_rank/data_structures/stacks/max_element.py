# prompt: https://www.hackerrank.com/challenges/maximum-element/problem

n = int(input())
stack = []
maxStack = [0]
for _ in range(n):
    comm = [int(x) for x in input().split(" ")]
    if comm[0] == 1:
        stack.append(comm[1])
        maxStack.append(max(comm[1], maxStack[-1]))
    if comm[0] == 2:
        stack.pop()
        maxStack.pop()
    if comm[0] == 3:
        print (maxStack[-1])
