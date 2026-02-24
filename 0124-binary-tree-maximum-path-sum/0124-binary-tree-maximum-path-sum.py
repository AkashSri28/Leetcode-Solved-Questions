# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = [float('-inf')]

        def node_sum(node):            
            if not node:
                return 0
            left_sum = max(node_sum(node.left), 0)
            right_sum = max(node_sum(node.right), 0)
            ans[0] = max(ans[0], node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)

        node_sum(root)
        return ans[0]
        