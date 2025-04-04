# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def LCA(node):
            if not node:
                return [None, 0]
            left = LCA(node.left)
            right = LCA(node.right)
            if left[1] == right[1]:
                return [node, left[1]+1]
            elif left[1] > right[1]:
                return [left[0], left[1]+1]
            return [right[0], right[1]+1]

        return LCA(root)[0]

        # TC: O(n)
        # SC: O(n)
        # Apporach: At each level we will LCA node and height. If we have 2 LCA at same height, then current node is LCA.
        