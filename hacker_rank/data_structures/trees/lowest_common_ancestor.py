# prompt: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    r1 = routeTo(root, v1)
    r2 = routeTo(root, v2)
    visited = []
    while len(r1) > 0 and len(r2) > 0:
        test_node1 = r1.pop()
        if test_node1 in visited:
            return test_node1
        visited.append(test_node1)
        test_node2 = r2.pop()
        if test_node2 in visited:
            return test_node2
        visited.append(test_node2)
    while len(r1) > 0:
        test_node1 = r1.pop()
        if test_node1 in visited:
            return test_node1
    while len(r2) > 0:
        test_node2 = r2.pop()
        if test_node2 in visited:
            return test_node2

def routeTo(root, value):
    if root.data == value:
        return [root]
    if value > root.data:
        route = [root] + routeTo(root.right, value)
    else:
        route = [root] + routeTo(root.left, value)
    return route
