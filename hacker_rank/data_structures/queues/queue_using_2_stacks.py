

# Simple solution using a single list
n = int(input())
queue = []
for _ in range(n):
    comm = input().split(" ")
    if comm[0] == '1':
        queue.append(comm[1])
    if comm[0] == '2':
        queue.pop(0)
    if comm[0] == '3':
        print(queue[0])

# Intended solution using two stacks

n = int(input())
addStack = []
popStack = []
for _ in range(n):
    comm = input().split(" ")
    if comm[0] == '1':
        addStack.append(comm[1])
    if comm[0] == '2':
        if len(popStack) == 0:
            while len(addStack) > 0:
                popStack.append(addStack.pop())
        popStack.pop()
    if comm[0] == '3':
        if len(popStack) == 0:
            while len(addStack) > 0:
                popStack.append(addStack.pop())
        print(popStack[-1])
