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
        lr = ListNode()
        ltmp = lr
        if l1 == None || l2 == None:
            return flase
        while true: 
            ltmp.val = l1.val + l2.val
            ltmp.next = ListNode() 
            ltmp = ltmp.next
            l1 = l1.next
            l2 = l2.next
            if l1 == None:
                ltmp = l2
                break
            if l2 == None:
                ltmp = l1
                break
        
        ltmp1 = ltmp
        ltmp2 = ltmp
        while ltmp.next != None:
            ltmp1 = ltmp2
            while ltmp1.next != None:
                ltmp1 = ltmp1.next 
            ltmp.val = ltmp1.val
            ltmp = ltmp.next
            ltmp1 = None
            ltmp = ltmp.next
        return ltmp
