"""
Note: Try to solve this task in O(m + n) or O(n) time, where n is a number of vertices and m is a number of edges, since this is what you'll be asked to do during an interview.

In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

Example

For connections = [[1], [2], [3, 4], [4], [0]], the output should be
hasDeadlock(connections) = true.


This graph contains a cycle.

For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
hasDeadlock(connections) = false.


This graph doesn't contain a directed cycle (there are two paths from 0 to 3, but no paths from 3 back to 0).

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer connections

A representation of the graphs edges. connection.length is the number of vertices. If j is in the list connections[i], then there is a directed edge from process i to process j.

Guaranteed constraints:
1 ≤ connections.length ≤ 500,
0 ≤ connections[i][j] < connections.length,
connections[i][j] ≠ connections[i][k] for j ≠ k,
i not in connections[i].

[output] boolean

Return True if connections describes a graph with a directed cycle, or False otherwise.
"""

def hasDeadlock(connections):
    graphDict = {}
    for idx, connection in enumerate(connections):
        graphDict[idx] = connection
    checked = [False for _ in connections]
    for nodeIdx, c in enumerate(checked):
        if c:
            continue
        paths = [[nodeIdx]]
        checked[nodeIdx] = True
        while paths:
            currPath = paths.pop()
            nextNodes = graphDict[currPath[-1]]
            for node in nextNodes:
                if node in currPath:
                    return True
                checked[node] = True
                paths.append(currPath + [node])
    return False
