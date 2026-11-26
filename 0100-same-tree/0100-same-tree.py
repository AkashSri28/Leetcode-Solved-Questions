# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkNodes(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.checkNodes(p.left, q.left) and self.checkNodes(p.right, q.right)

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.checkNodes(p, q)
        