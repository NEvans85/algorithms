# prompt: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    visited = [headA, headB]
    nodeA = headA.next
    nodeB = headB.next
    while nodeA and nodeB:
        if nodeA in visited or nodeA == nodeB:
            return nodeA.data
        elif nodeB in visited:
            return nodeB.data
        else:
            visited.append(nodeA)
            visited.append(nodeB)
            nodeA = nodeA.next
            nodeB = nodeB.next
    while nodeA:
        if nodeA in visited:
            return nodeA.data
        else:
            nodeA = nodeA.next
    while nodeB:
        if nodeB in visited:
            return nodeB.data
        else:
            nodeB = nodeB.next