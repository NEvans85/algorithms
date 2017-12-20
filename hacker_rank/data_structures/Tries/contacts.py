# prompt: https://www.hackerrank.com/challenges/contacts/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.wordCount = 1

    def getChild(self, data):
        for child in self.children:
            if child.data == data:
                return child
        return False

    def addChild(self, data):
        newNode = Node(data)
        self.children.append(newNode)
        return newNode

    def incCount(self, amt = 1):
        self.wordCount += 1

    def countWords(self):
        return self.wordCount


def addWord(word, root):
    currNode = root
    for ch in word:
        nextNode = currNode.getChild(ch)
        if nextNode:
            nextNode.incCount()
            currNode = nextNode
        else:
            currNode = currNode.addChild(ch)

def countEntries(str, root):
    currNode = root
    for ch in str:
        nextNode = currNode.getChild(ch)
        if nextNode:
            currNode = nextNode
        else:
            return 0
    return currNode.countWords()

n = int(input())
root = Node("_")
for _ in range(n):
    action, word = input().split(" ")
    if action == "add":
        addWord(word, root)
    if action == "find":
        print(countEntries(word, root))
