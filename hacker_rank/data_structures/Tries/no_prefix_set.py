# prompt: https://www.hackerrank.com/challenges/no-prefix-set/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def getChild(self, data):
        for child in self.children:
            if child.data == data:
                return child
        return False

    def addChild(self, data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

def addWord(word, root):
    word += "$"
    currNode = root
    pCheck2 = True
    for ch in word:
        prefixCheck = currNode.getChild("$")
        if prefixCheck:
            return False
        else:
            nextNode = currNode.getChild(ch)
            if nextNode:
                currNode = nextNode
                pCheck2 = True
            else:
                currNode = currNode.addChild(ch)
                if ch != "$":
                    pCheck2 = False
    if pCheck2:
        return False
    return True

root = Node("_")
n = int(input())
good = True
for _ in range(n):
    word = input()
    if not addWord(word, root):
        print ("BAD SET")
        print (word)
        good = False
        break
if good:
    print ("GOOD SET")
