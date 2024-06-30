# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        f = curr.next
        while f.next is not None:
            curr.val = f.val
            curr = f
            f = f.next
        curr.val = f.val
        curr.next = None
        
        