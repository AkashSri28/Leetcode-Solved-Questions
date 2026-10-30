# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, node, p, q):
        if not node or node == p or node == q:
            return node

        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right:
            return node

        return left or right
        
# Clarification: if a node can be ancestor of itself
# Brute Force: for each node we can check if it contains both p and q 
# Approach: using dfs we can iterate all nodes and check whenever a node has both children, will true if a node is found
# TC: O(n)
# SC: O(h)
# Testing: check we children are not there in tree