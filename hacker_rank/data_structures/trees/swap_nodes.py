# prompt: https://www.hackerrank.com/challenges/swap-nodes-algo/problem

class Node:
    def __init__(self, value, left_node = None, right_node = None):
        self.data = value
        self.left = left_node
        self.right = right_node

def swap(root):
    root.left, root.right = root.right, root.left
    return True

def nodesAtNHeight(root, h):
    search_queue = [root]
    results = []
    n = 1
    height = 1
    while len(search_queue) > 0:
        if height == n * h:
            results += search_queue
            n += 1
        children = []
        for node in search_queue:
            children += [el for el in [node.left, node.right] if el.data != -1]
        search_queue = children
        height += 1
    return results

# recursive in order traversial causes stack overflow in "tall" trees
def inOrder(root):
    results = visit(root)
    print(" ".join([str(x) for x in results]))

def visit(root):
    values = []
    if root.left:
        values += visit(root.left)
    if root.data != -1:
        values.append(root.data)
    if root.right:
        values += visit(root.right)
    return values

n = int(input())
root = Node(1)
build_queue = [root]
for _ in range(n):
    ch_data = [int(el) for el in input().split(" ")]
    curr_node = build_queue.pop(0)
    curr_node.left = Node(ch_data[0])
    if ch_data[0] != -1:
        build_queue.append(curr_node.left)
    curr_node.right = Node(ch_data[1])
    if ch_data[1] != -1:
        build_queue.append(curr_node.right)
q = int(input())
for _ in range(q):
    h = int(input())
    for node in nodesAtNHeight(root, h):
        swap(node)
    inOrder(root)
