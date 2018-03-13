"""
You have a connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the graph.

Example

For

g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]
and s = 0, the output should be
graphDistances(g, s) = [0, 2, 2].



The distance from the start vertex 0 to itself is 0.
The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
The distance from the start vertex 0 to vertex 2 is 2.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer g

The graph is represented as a square matrix, as described above.

Guaranteed constraints:
1 ≤ g.length ≤ 100,
g.length = g[i].length,
-1 ≤ g[i][j] ≤ 30.

[input] integer s

The start vertex (0-based).

Guaranteed constraints:
0 ≤ s < g.length.

[output] array.integer

An array, the ith element of which is equal to the distance between the start vertex s and the ith vertex of the graph g.
"""

# The following uses Djikstra's Algorithm to find the shortest path to each node

def graphDistances(g, s):
    dist = [float('inf') for _ in g]
    dist[s] = 0
    visited = [False for _ in g]
    currNode = s
    visited[currNode] = True
    nodeQ = []
    while any(not v for v in visited):
        neighbors = [idx for idx, w in enumerate(g[currNode]) if w > -1 and not visited[idx]]
        for nIdx in neighbors:
            legDist = g[currNode][nIdx]
            dist[nIdx] = min(dist[nIdx], dist[currNode] + legDist)
        sNeighbors = sorted(neighbors, key=lambda x: dist[x])
        nodeQ = sNeighbors + nodeQ
        currNode = nodeQ.pop(0)
        visited[currNode] = True
    return dist
