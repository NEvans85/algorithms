# prompt: https://www.hackerrank.com/challenges/simple-text-editor/problem

n = int(input())
cStack = []
s = "_"
for _ in range(n):
    comm = input().split(" ")
    if comm[0] == '1':
        s += comm[1]
        cStack.append(comm)
    if comm[0] == '2':
        d = int(comm[1])
        comm.append(s[(-1 * d):])
        s = s[:(-1 * d)]
        cStack.append(comm)
    if comm[0] == '3':
        p = int(comm[1])
        print (s[p])
    if comm[0] == '4':
        u = cStack.pop()
        if u[0] == '1':
            d = len(u[1])
            s = s[:(-1 * d)]
        if u[0] == '2':
            s += u[2]
