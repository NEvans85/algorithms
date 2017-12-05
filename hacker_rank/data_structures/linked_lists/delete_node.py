# prompt: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        curr_pos = 1
        prev = head
        curr_node = head.next
        while curr_pos < position:
            curr_pos += 1
            prev = curr_node
            curr_node = curr_node.next
        prev.next = curr_node.next
        return head