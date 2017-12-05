# prompt: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visited = []
    node = head
    while node and node.next:
        visited.append(node)
        node = node.next
        if node in visited:
            return True
    return False