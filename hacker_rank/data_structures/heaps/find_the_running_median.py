# prompt: https://www.hackerrank.com/challenges/find-the-running-median/problem

"""
This solution uses a pair of heaps (a min heap and a max heap) to store
the lower and upper half of the inputs. As each value is inserted, the
heaps are adjusted to keep their size within one of each other. This
optimizes the action of finding the median as one need only view the
root of the larger of the two heaps or take the average of the two roots
in the event that they are the same size.
"""

class heap:
    def __init__(self):
        self.store = [0]
        self.currentSize = 0

    def size(self):
        return self.currentSize

    def insert(self, value):
        self.store.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def peekRoot(self):
        return self.store[1]

    def deleteRoot(self):
        rootVal = self.store[1]
        self.store[1] = self.store[self.currentSize]
        self.store.pop()
        self.currentSize -= 1
        self.percDown(1)
        return rootVal

class minHeap(heap):

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx] < self.store[idx // 2]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2

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

class maxHeap(heap):

    def percUp(self, idx):
        while idx // 2 > 0:
            if self.store[idx] > self.store[idx // 2]:
                temp = self.store[idx // 2]
                self.store[idx // 2] = self.store[idx]
                self.store[idx] = temp
            idx = idx // 2

    def percDown(self, idx):
        while idx * 2 <= self.currentSize:
            lc = self.largestChild(idx)
            if self.store[idx] < self.store[lc]:
                temp = self.store[lc]
                self.store[lc] = self.store[idx]
                self.store[idx] = temp
            idx = lc

    def largestChild(self, idx):
        if idx * 2 + 1 > self.currentSize or self.store[idx * 2] > self.store[idx * 2 + 1]:
            return idx * 2
        else:
            return idx * 2 + 1

n = int(input())
high = minHeap()
low = maxHeap()
firstInt = int(input())
low.insert(firstInt)
print(round(firstInt, 1))
for _ in range(n - 1):
    newInt = int(input())
    if newInt > low.peekRoot():
        high.insert(newInt)
    else:
        low.insert(newInt)
    if low.size() - high.size() > 1:
        toMove = low.deleteRoot()
        high.insert(toMove)
    elif high.size() - low.size() > 1:
        toMove = high.deleteRoot()
        low.insert(toMove)
    if low.size() > high.size():
        median = low.peekRoot()
    elif high.size() > low.size():
        median = high.peekRoot()
    else:
        median = (low.peekRoot() + high.peekRoot()) / 2
    print(round(median, 1))
