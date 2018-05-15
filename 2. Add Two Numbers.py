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
        res1 = l1
        res2 = l2
        len1 = 0
        len2 = 0
        last1 = l1
        last2 = l2
        while l1 != None or l2 != None :
            if l1 == None :
                if l2.val > 9:
                    l2.val = l2.val%10
                    if l2.next == None :
                        last2.next = ListNode(1)
                        len2 += 1
                    else :
                        l2.next.val += 1
                len2 += 1
                if l2.next != None :
                    last2 = l2.next
                l2 = l2.next
            elif l2 == None :
                if l1.val > 9:
                    l1.val = l1.val%10
                    if l1.next == None :
                        last1.next = ListNode(1)
                    else :
                        l1.next.val += 1
                len1 += 1
                if l1.next != None :
                    last1 = l1.next
                l1 = l1.next
            else :
                tmp = l1.val + l2.val
                l1.val = tmp%10
                l2.val = tmp%10
                if tmp > 9 :
                    if l1.next != None :
                        l1.next.val += 1
                    else :
                        last1.next = ListNode(1)
                len1 += 1
                len2 += 1
                if l1.next != None :
                    last1 = l1.next
                if l2.next != None :
                    last2 = l2.next
                l1 = l1.next
                l2 = l2.next
        if len2 > len1 :
            return res2
        else :
            return res1
