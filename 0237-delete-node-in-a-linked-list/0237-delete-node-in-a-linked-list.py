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
        curr = node.next
        node.val = curr.val
        node.next = curr.next
        
# TC: O(1)
# SC: O(1)
# Approach1: Trick Question, just keep copying data from next node and delete last node
# Better Approach: just copy data from next node to curr and skip next
        