# prompt: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    node = head
    while node and node.next:
        prev_node = node
        node = node.next
        while node and prev_node.data == node.data:
            prev_node.next = node.next
            node = node.next
    return head