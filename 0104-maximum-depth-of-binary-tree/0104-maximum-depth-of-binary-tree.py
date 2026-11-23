# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDepth(self, node, depth):
        if node:
            self.md = max(self.md, depth)
            self.findDepth(node.left, depth+1)
            self.findDepth(node.right, depth+1)

    def maxDepth(self, root: TreeNode | None) -> int:
        self.md = 0
        self.findDepth(root, 1)
        return self.md
        
# TC: O(n) DFS
# SC: O(n)
# Approach: 