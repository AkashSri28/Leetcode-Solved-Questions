# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = 0
        node = head
        while node:
            cnt += 1
            node = node.next
            
        d, r = cnt//k, cnt%k
        node = head
        ans = []
        for i in range(k):
            if not node:
                ans.append(None)
            else:
                cnt = 1
                ans.append(node)
                prev = None
                while node and cnt <= d:
                    cnt += 1
                    prev = node
                    node = node.next

                if r > 0:
                    r -= 1
                    prev = node
                    node = node.next
                    
                prev.next = None
        
        return ans
                
        
        