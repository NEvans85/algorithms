# prompt: https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# THis is my first try at the solution. It is long and repeats code in several places.
# I believe that it can be made much more efficient.
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        num1 = l1.val
        num2 = l2.val
        numR = num1 + num2 + carry
        if numR > 9:
            carry = 1
            numR %= 10
        else:
            carry = 0
        currNode1 = l1
        currNode2 = l2
        resultHead = ListNode(numR)
        currNodeR = resultHead
        while  currNode1.next != None and currNode2.next != None:
            currNode1 = currNode1.next
            currNode2 = currNode2.next
            num1 = currNode1.val
            num2 = currNode2.val
            numR = num1 + num2 + carry
            if numR > 9:
                carry = 1
                numR %= 10
            else:
                carry = 0
            currNodeR.next = ListNode(numR)
            currNodeR = currNodeR.next
        while currNode1.next:
            currNode1 = currNode1.next
            numR = currNode1.val + carry
            if numR > 9:
                carry = 1
                numR %= 10
            else:
                carry = 0
            currNodeR.next = ListNode(numR)
            currNodeR = currNodeR.next
        while currNode2.next:
            currNode2 = currNode2.next
            numR = currNode2.val + carry
            if numR > 9:
                carry = 1
                numR %= 10
            else:
                carry = 0
            currNodeR.next = ListNode(numR)
            currNodeR = currNodeR.next
        if carry == 1:
            currNodeR.next = ListNode(carry)
        return resultHead
