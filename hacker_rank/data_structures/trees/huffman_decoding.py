# prompt: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    result = ""
    node = root
    for ch in s:
        if ch == '1':
            if leaf(node.right):
                result += leaf(node.right)
                node = root
            else:
                node = node.right
        else:
            if leaf(node.left):
                result += leaf(node.left)
                node = root
            else:
                node = node.left
    print result

def leaf(node):
    if node.left or node.right:
        return False
    else:
        return node.data
