# prompt: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head.next:
        prev = head
        curr_node = head.next
        prev.next = None
        while curr_node.next:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        curr_node.next = prev
        return curr_node
    else:
        return head