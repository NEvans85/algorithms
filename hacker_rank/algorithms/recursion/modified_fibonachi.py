# prompt: https://www.hackerrank.com/challenges/fibonacci-modified/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
rawInputList = input().split(" ")
intInputList = [int(x) for x in rawInputList]
store = [intInputList[0], intInputList[1]]
n = intInputList[2]

def modFib(n):
    for x in range(2, n):
        store.append(store[x - 2] + store[x - 1] ** 2)
    return store[n - 1]

print (modFib(n))