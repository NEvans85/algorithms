# prompt: https://www.hackerrank.com/challenges/30-binary-trees/problem

def levelOrder(self,root):
    if root:
        queue = [root]
    else:
        return []
    values = []
    while len(queue) > 0:
        nextEl = queue.pop()
        if nextEl.left:
            queue.insert(0, nextEl.left)
        if nextEl.right:
            queue.insert(0, nextEl.right)
        values.append(nextEl.data)
    print(" ".join([str(x) for x in values]))
