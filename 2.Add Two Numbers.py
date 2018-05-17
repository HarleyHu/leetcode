# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1 :
                val1 = l1.val
                l1 = l1.next
            if l2 :
                val2 = l2.val
                l2 = l2.next
            sum = val1 + val2 + carry
            p.next = ListNode(sum%10)
            carry = sum//10
            p = p.next
        return res.next
