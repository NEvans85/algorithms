# prompt: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if not head or not head.next:
        return head
    node = head
    while node.next:
        prev = node
        node = node.next
        prev.next, prev.prev = prev.prev, prev.next
    node.next, node.prev = node.prev, node.next
    return node