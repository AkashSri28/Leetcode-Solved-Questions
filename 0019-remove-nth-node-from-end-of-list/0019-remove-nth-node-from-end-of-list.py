# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p, q = head, head
        for _ in range(n):
            p = p.next

        if p == None:
            return q.next

        while p.next:
            p = p.next
            q = q.next

        q.next = q.next.next
        return head

        # TC: O(n)
        # SC: O(1)
        # Approach: use 2 pointers with distance n, to find n-1 node. Then point n-1th node to n.next.next. This will skip nth node. Explicitly deleting node is not required
        

        