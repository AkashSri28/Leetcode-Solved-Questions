# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base cases
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        # Check if they are equivalent without flip or with flip
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
    (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
    
    # TC: O(min(n, m))
    #     SC: O(min(h1, h2))
    #         Approach: check with and without flip to see if nodes match
        
            
        
        