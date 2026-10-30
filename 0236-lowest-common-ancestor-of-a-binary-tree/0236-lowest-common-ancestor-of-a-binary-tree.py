# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        self.dfs(root, p, q)
        return self.ans

    def dfs(self, node, p, q):
        if not node:
            return False

        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right and not self.ans:
            self.ans = node

        if (node == p or node == q) and (left or right) and not self.ans:
            self.ans = node

        return (node == p) | (node == q) | left | right
        