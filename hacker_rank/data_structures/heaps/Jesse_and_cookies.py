# prompt: https://www.hackerrank.com/challenges/jesse-and-cookies/problem

# This solution still times out on very large test sets (cases 20 - 23).

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

    def deleteMin(self):
        minVal = self.store[1]
        self.store[1] = self.store[self.currentSize]
        self.store.pop()
        self.currentSize -= 1
        self.percDown(1)
        return minVal

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

    def buildHeap(self, iList):
        idx = len(iList) // 2
        self.currentSize = len(iList)
        self.store = [0] + iList[:]
        while (idx > 0):
            self.percDown(idx)
            idx -= 1

n, k = [int(x) for x in input().split(" ")]
h = Heap()
h.buildHeap([int(x) for x in input().split(" ")])
oppCount = 0
minC = h.deleteMin()
while h.currentSize > 0 and minC < k:
    minC2 = h.deleteMin()
    newC = minC + minC2 * 2
    h.insert(newC)
    minC = h.deleteMin()
    oppCount += 1
if minC >= k:
    print(oppCount)
else:
    print(-1)
