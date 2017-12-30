# prompt: https://www.hackerrank.com/challenges/components-in-graph/problem

# This solution still fails case 2 and 9. There is some problem in assigning
# the minSet.

class disjointSet:
    def __init__(self):
        self.store = {}
        self.maxSet = None
        self.minSet = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = self
            self.rank = 0
            self.setSize = 1

    def makeSet(self, data):
        newNode = self.Node(data)
        self.store[data] = newNode

    def union(self, data1, data2):
        root1 = self.findSet(data1)
        root2 = self.findSet(data2)
        if root1.data != root2.data:
            if root1.rank == root2.rank:
                root1.rank += 1
            if root1.rank >= root2.rank:
                root2.parent = root1
                root1.setSize += root2.setSize
                root = root1
            else:
                root1.parent = root2
                root2.setSize += root1.setSize
                root = root2
            if self.maxSet == None or root.setSize > self.maxSet.setSize:
                self.maxSet = root
            if self.minSet:
                self.minSet = self.findSet(self.minSet.data)
            if self.minSet == None or root.setSize <= self.minSet.setSize:
                self.minSet = root


    def findSet(self, data):
        node = self.store[data]
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.findSet(node.parent.data)
        return node.parent

n = int(input())
ds = disjointSet()
for i in range(1, 1 + 2 * n):
    ds.makeSet(i)
for _ in range(n):
    g, b = [int(x) for x in input().split(" ")]
    ds.union(g, b)
maxSize = ds.maxSet.setSize
minSize = ds.minSet.setSize
print(" ".join([str(x) for x in [minSize, maxSize]]))
