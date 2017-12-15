# prompt: https://www.hackerrank.com/challenges/is-binary-search-tree/problem

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    trav = inOrder(root)
    return trav == sorted(trav) and list(set(trav)) == trav

def inOrder(root):
    values = []
    if root.left:
        values += inOrder(root.left)
    values.append(root.data)
    if root.right:
        values += inOrder(root.right)
    return values
