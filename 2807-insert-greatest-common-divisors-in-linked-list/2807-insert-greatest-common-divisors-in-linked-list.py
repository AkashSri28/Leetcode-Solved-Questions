# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b > a:
                return gcd(b, a)
            if b == 0:
                return a
            return gcd(b, a%b)
        
        curr, future = head, head.next
        while future:
            value = gcd(curr.val, future.val)
            new_node = ListNode(value, future)
            curr.next = new_node
            curr = future
            future = future.next
            
        return head
        
    # TC: O(n) #all nodes need to be traversed
    # SC: O(1) #only pointers are used
    # Approach: Use 2 pointer to point to 2 nodes. Find gcd and insert between 2 nodes.    