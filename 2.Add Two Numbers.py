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
        p = ListNode(0)
        res = p
        carry = 0
        while l1 or l2 or carry:
            if l1 == None and l2 :
                sum = l2.val + carry
                p.next = ListNode(sum%10)
                p = p.next
                l2 = l2.next
                carry = sum//10
                continue
            if l1 and l2 == None :
                sum = l1.val + carry
                p.next = ListNode(sum%10)
                p = p.next
                l1 = l1.next
                carry = sum//10
                continue
            if l1 == None and l2 == None :
                p.next = ListNode(carry)
                p = p.next
                carry = 0
                continue
            sum = l1.val + l2.val + carry
            p.next = ListNode(sum%10)
            carry = sum//10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        return res.next
