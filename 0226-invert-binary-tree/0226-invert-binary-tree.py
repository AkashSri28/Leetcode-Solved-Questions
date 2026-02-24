# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def swap_children(node):
            if not node:
                return 

            left = node.left
            node.left = node.right
            node.right = left
            swap_children(node.left)
            swap_children(node.right)

        swap_children(root)
        return root
        