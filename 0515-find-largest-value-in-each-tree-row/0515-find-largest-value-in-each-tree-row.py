# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        ans = []
        
        while q:
            level_max = float('-inf')
            for i in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_max)
        
        return ans
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: use BFS to read node at each level and then find max at that level
        
        