# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, 0)]

        while stack:
            node, p = stack.pop()
            if p == 0:
                stack.append((node, 1))
                if node.left:
                    stack.append((node.left, 0))
            elif p == 1:
                res.append(node.val)
                if node.right:
                    stack.append((node.right, 0))
            
        return res

        