def removeDuplicates(self,head):
    seen = []
    nextNode = head
    while nextNode:
        if nextNode.data not in seen:
            seen.append(nextNode.data)
            prevNode = nextNode
            nextNode = nextNode.next
        else:
            prevNode.next = nextNode.next
            nextNode = nextNode.next
    return head
