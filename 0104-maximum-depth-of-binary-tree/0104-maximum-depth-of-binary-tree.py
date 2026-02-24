# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def find_depth(node):
            if not node:
                return 0
            return max(find_depth(node.left), find_depth(node.right)) + 1

        return find_depth(root)

        # TC: O(n)
        # SC: O(n) # recursion depth
        # Approach: null node will have 0 depth. Other nodes will have 1 + max of depth of its children