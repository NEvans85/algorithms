# prompt: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        pos = 1
        node = head
        while pos < position:
            pos += 1
            node = node.next
        if node.next:
            prev = node.next
            node.next = Node(data, prev)
        else:
            node.next = Node(data)
        return head