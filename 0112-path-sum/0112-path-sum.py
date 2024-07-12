# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, curr, targetSum):
            if(not node):
                return False
            if(node and not node.left and not node.right):
                if(curr+node.val == targetSum):
                    return True
                return False
            return dfs(node.left, curr+node.val, targetSum) or dfs(node.right, curr+node.val, targetSum)
        
        return dfs(root, 0 ,targetSum)
        