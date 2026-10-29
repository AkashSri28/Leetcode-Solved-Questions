# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def findDiameterAtNode(node):
            if node:
                nonlocal ans
                left = findDiameterAtNode(node.left)
                right = findDiameterAtNode(node.right)
                ans = max(ans, left + right)
                return 1 + max(left, right)

            return 0

        findDiameterAtNode(root)
        return ans

# TC: O(n)
# SC: O(h)
        