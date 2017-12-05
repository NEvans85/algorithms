# prompt: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    values = []
    if head:
        values.append(head.data)
        next_node = head
        while next_node.next:
            next_node = next_node.next
            values.append(next_node.data)
    while len(values) > 0:
        print (values.pop())