# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def swapNodes(node):
            if node:
                node.left, node.right = node.right, node.left
                swapNodes(node.left)
                swapNodes(node.right)

        swapNodes(root)
        return root
        