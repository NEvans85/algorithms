# prompt https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

"""
 Compare two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 1 if equal, 0 if not equal.
"""

def CompareLists(headA, headB):
    nodeA = headA
    nodeB = headB
    while nodeA and nodeB:
        if nodeA.data != nodeB.data:
            return 0
        nodeA = nodeA.next
        nodeB = nodeB.next
    if nodeA or nodeB:
        return 0
    else:
        return 1