# prompt: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    child_heights = []
    if root.left:
        child_heights.append(height(root.left))
    if root.right:
        child_heights.append(height(root.right))
    if len(child_heights) == 0:
        return 0
    best_child = max(child_heights)
    return (1 + best_child)