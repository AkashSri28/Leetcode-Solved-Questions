# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1, p2 = head, head.next
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        stack = []
        p2 = p1
        p1 = p1.next
        p2.next = None
        while p1:
            stack.append(p1)
            p1 = p1.next

        p1 = head
        while stack:
            node = stack.pop()
            node.next = p1.next
            p1.next = node
            p1 = node.next
            



        

        