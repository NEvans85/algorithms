# prompt: https://www.hackerrank.com/challenges/merging-communities/problem

class disjointSet:
    def __init__(self):
        self.store = {}

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
            else:
                root1.parent = root2
                root2.setSize += root1.setSize


    def findSet(self, data):
        node = self.store[data]
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.findSet(node.parent.data)
        return node.parent

n, q = [int(x) for x in input().split(" ")]
ds = disjointSet()
for i in range(1, n + 1):
    ds.makeSet(i)
for _ in range(q):
    query = input().split(" ")
    if query[0] == "Q":
        print ((ds.findSet(int(query[1]))).setSize)
    if query[0] == "M":
        data1 = int(query[1])
        data2 = int(query[2])
        ds.union(data1, data2)
