# prompt: https://www.hackerrank.com/challenges/bfsshortreach/problem

import sys

class Tree:
    def __init__(self, numNodes):
        self.connMatrix = [[0 for col in range(numNodes + 1)] for row in range(numNodes + 1)]

    def bfs(self, start, target):
        visited = [0 for _ in range(len(self.connMatrix) + 1)]
        queue = [[start]]
        while len(queue) != 0:
            path = queue.pop(0)
            node = path[-1]
            if node == target:
                return path
            visited[node] = 1
            for idx in range(len(self.connMatrix[node])):
                if self.connMatrix[node][idx] == 1 and visited[idx] == 0:
                    queue.append(path + [idx])
        return []


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        tree = Tree(n)
        for a1 in range(m):
            u, v = input().strip().split(' ')
            u, v = [int(u), int(v)]
            tree.connMatrix[u][v] = 1
            tree.connMatrix[v][u] = 1
        s = int(input().strip())
        targets = [x for x in range(1, n + 1) if x != s]
        results = []
        for t in targets:
            path = tree.bfs(s, t)
            if path:
                results.append((len(path) - 1) * 6)
            else:
                results.append(-1)
        print (" ".join([str(x) for x in results]))
