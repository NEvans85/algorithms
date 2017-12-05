# prompt: https://www.hackerrank.com/challenges/tree-top-view/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    results = []
    if root.left:
        results += left(root.left)
    results.append(root.data)
    if root.right:
        results += right(root.right)
    print(" ".join([str(x) for x in results]))

def left(root):
    if root.left:
        return left(root.left) + [root.data]
    else:
        return [root.data]

def right(root):
    if root.right:
        return [root.data] + right(root.right)
    else:
        return [root.data]