# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        self.ans = []
        self.seen = set()

        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, level):
        if not node:
            return
        if level not in self.seen:
            self.seen.add(level)
            self.ans.append(node.val)
        self.dfs(node.right, level+1)
        self.dfs(node.left, level+1)
        return