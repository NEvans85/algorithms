# prompt: https://www.hackerrank.com/challenges/30-binary-search-trees/problem

def getHeight(self,root):
    if root.right == None and root.left == None:
        return 0
    childHeights = []
    for child in [x for x in [root.right, root.left] if x != None]:
        childHeights.append(1 + self.getHeight(child))
    return max(childHeights)
