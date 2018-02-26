# prompt: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from collections import defaultdict

class Graph:
    def __init__(self, numNodes):
        self.edgeDict = defaultdict(set)
        self.n = numNodes

    def connect(self, a, b):
        self.edgeDict[a].add(b)
        self.edgeDict[b].add(a)

    def find_all_distances(self, node):
        bfsQ = [node]
        distances = [-1 for _ in range(self.n)]
        distances[node] = 0
        while len(bfsQ) > 0:
            currNode = bfsQ.pop(0)
            nextNodes = [el for el in self.edgeDict[currNode] if distances[el] == -1]
            for nIdx in nextNodes:
                distances[nIdx] = distances[currNode] + 6
                bfsQ.append(nIdx)
        distances.pop(node)
        print(*distances)

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
