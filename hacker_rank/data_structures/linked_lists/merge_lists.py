# prompt: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA and headB:
        nodeA = headA
        nodeB = headB
        if nodeA.data > nodeB.data:
            new_head = nodeB
            nodeB = nodeB.next
        else:
            new_head = nodeA
            nodeA = nodeA.next
        curr_node = new_head
        while nodeA and nodeB:
            if nodeA.data > nodeB.data:
                curr_node.next = nodeB
                nodeB = nodeB.next
            else:
                curr_node.next = nodeA
                nodeA = nodeA.next
            curr_node = curr_node.next
        if nodeA:
            curr_node.next = nodeA
        elif nodeB:
            curr_node.next = nodeB
        return new_head
    elif headA:
        return headA
    else:
        return headB