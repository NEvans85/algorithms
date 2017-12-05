# prompt: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    results = visit(root)
    print(" ".join([str(x) for x in results]))
    
def visit(root):
    values = [root.data]
    if root.left:
        values += visit(root.left)
    if root.right:
        values += visit(root.right)
    return values