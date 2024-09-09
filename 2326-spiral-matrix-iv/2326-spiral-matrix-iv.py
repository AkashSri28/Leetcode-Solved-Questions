# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        node = head
        i, j, k, l = 0, n-1, m-1, 0
        ans = [[-1]*n for _ in range(m)]
        while i <= k and l <= j:
            loop = l
            while loop <= j:
                if node:
                    ans[i][loop] = node.val
                    node = node.next
                loop += 1
            i += 1
            
            loop = i
            while loop <= k:
                if node:
                    ans[loop][j] = node.val
                    node = node.next
                loop += 1
            j -= 1
            
            loop = j
            while loop >= l:
                if node:
                    ans[k][loop] = node.val
                    node = node.next
                loop -= 1
            k -= 1
                    
            loop = k
            while loop >= i:
                if node:
                    ans[loop][l] = node.val
                    node = node.next
                loop -= 1
            l += 1            
                    
        return ans
    
    # TC: O(m*n)
    #     SC: O(m*n)
    #         Approach: Use 4 pointer technique to mark inclusive boundaries. Now iterate and remove each boundary.
                
        
        