# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = 0
        while head:
            curr = curr*2 + head.val
            head = head.next

        return curr

        # TC: O(n)
        # SC: O(1)
        # Approach: we can iterate over LL and find bits, when a new bit is added, current value is multiplied with 2
        