# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = defaultdict(int)
        
        pair = (root, 0)    #(node, level)
        queue = deque()
        queue.append(pair)
        
        while queue:
            node, level = queue.popleft()
            level_sum[level] += node.val
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
                
        total = sorted(level_sum.values())
        total.reverse()
        
        n = len(total)
        if n < k:
            return -1
        
        return total[k-1]
    
    # TC: O(n) + O(nlogn)
    #     SC: O(n)
    #         Approach: Store level wise sum using BFS in dict. Sort values and return kth largest.
            
        