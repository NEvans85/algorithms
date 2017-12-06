# prompt: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if r:
        if r.data < val:
            if r.right:
                insert(r.right, val)
            else:
                r.right = Node(val)
        else:
            if r.left:
                insert(r.left, val)
            else:
                r.left = Node(val)
    else:
        r = Node(val)
    return r
