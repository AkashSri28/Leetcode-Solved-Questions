# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, prev, head = 0, None, None
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val/10
            val = val%10
            newNode = ListNode(val)
            if not prev:
                head = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            carry = val/10
            val = val%10
            newNode = ListNode(val)
            if not prev:
                head = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode
            l1 = l1.next
        while l2:
            val = l2.val + carry
            carry = val/10
            val = val%10
            newNode = ListNode(val)
            if not prev:
                head = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode
            l2 = l2.next
        if carry > 0:
            newNode = ListNode(carry)
            prev.next = newNode
            
        return head
            
        