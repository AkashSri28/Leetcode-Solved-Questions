# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        new_head = head
        
        while new_head and new_head.val in nums_set:
            new_head = new_head.next
            
        if not new_head:
            return new_head
        
        curr, new = new_head, new_head.next
        
        while new:
            if new.val not in nums_set:
                curr.next = new
                curr = new
            new = new.next
            
        curr.next = None
        
        
        return new_head
        