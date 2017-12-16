# prompt: https://www.hackerrank.com/challenges/equal-stacks/problem

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

# A Cylinder Stack class is defined so that the height of each can be tracked
# rather than summed up each time.
class CylStack:
    def __init__(self, content):
        self.store = content
        self.height = sum(self.store)

    def pop(self):
        top = self.store.pop(0)
        self.height -= top

# height is defined here for use as a key in the max funtion in the while loop
# and for determining equality of all stacks
def height(cStack):
    return cStack.height

stacks = [CylStack(h1), CylStack(h2), CylStack(h3)]

# The list of stacks is converted to a set of the stack's heights to determine
# if all are equal. The loop removes the top element fo the tallest stack
# until the stacks are all equal height.
while len(set([height(x) for x in stacks])) > 1:
    tallest = max(stacks, key = height)
    tallest.pop()

print (height(stacks[0]))
