# prompt: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    queue = [root]
    results = []
    while len(queue) > 0:
        curr_node = queue.pop(0)
        results.append(curr_node.data)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    print (" ".join([str(x) for x in results]))
