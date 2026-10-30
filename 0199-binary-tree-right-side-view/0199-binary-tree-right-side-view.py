# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        self.ans = []

        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, level):
        if not node:
            return
        if level == len(self.ans):
            self.ans.append(node.val)

        self.dfs(node.right, level+1)
        self.dfs(node.left, level+1)
        return

# Clarification: 
# Brute Force:
# Approach: Will do dfs and check for right child first
# TC: O(n)
# SC: O(h)
# Testing: will check null root, skewed trees