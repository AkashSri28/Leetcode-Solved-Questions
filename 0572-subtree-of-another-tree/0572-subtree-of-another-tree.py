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

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if self.checkNodes(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

# TC: O(n*n)  BFS*checkNodes()
# SC: O(h) deque
# Approach: use BFS to iterate over nodes in root, now check for subtree at each node if it matches with subtree