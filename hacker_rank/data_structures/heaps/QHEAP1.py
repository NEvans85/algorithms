# prompt: https://www.hackerrank.com/challenges/qheap1/problem

class Heap:
    def __init__(self):
        self.store = [0]
        self.currentSize = 0

    def insert(self, value):
        self.store.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx] < self.store[idx // 2]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2

    def delete(self, value):
        idx = self.store.index(value)
        self.store[idx] = self.store[self.currentSize]
        self.store.pop()
        self.currentSize -= 1
        self.percDown(idx)

    def percDown(self, idx):
        while idx * 2 <= self.currentSize:
            sc = self.smallestChild(idx)
            if self.store[idx] > self.store[sc]:
                temp = self.store[sc]
                self.store[sc] = self.store[idx]
                self.store[idx] = temp
            idx = sc

    def smallestChild(self, idx):
        if idx * 2 + 1 > self.currentSize or self.store[idx * 2] < self.store[idx * 2 + 1]:
            return idx * 2
        else:
            return idx * 2 + 1

    def printMin(self):
        print (self.store[1])

n = int(input())
h = Heap()
for _ in range(n):
    comm = [int(x) for x in input().split(" ")]
    if comm[0] == 1:
        h.insert(comm[1])
    elif comm[0] == 2:
        h.delete(comm[1])
    elif comm[0] == 3:
        h.printMin()
