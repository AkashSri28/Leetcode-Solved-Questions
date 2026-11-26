# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diaAtNode(self, node):
        if not node:
            return 0
        left = self.diaAtNode(node.left)
        right = self.diaAtNode(node.right)
        self.ans = max(self.ans, left+right)
        return 1+max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diaAtNode(root)
        return self.ans
        