# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        new_head = ListNode()
        new_head.next = head
        
        curr, new = new_head, new_head.next
        
        while new:
            if new.val not in nums_set:
                curr.next = new
                curr = new
            new = new.next
            
        curr.next = None        
        
        return new_head.next
        
    # TC: O(len(nums)+len(list))
    #     SC: O(len(nums))
    #         Approach: Here a trick is used. Whenever we need to delete nodes and head can also get delete, add a dummy node which points to head. 