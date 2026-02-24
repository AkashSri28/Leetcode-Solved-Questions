# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def check_node(node1, node2):
            if not node1 and not node2:
                return True

            if node1 and node2:
                if node1.val == node2.val:
                    return check_node(node1.left, node2.left) and check_node(node1.right, node2.right)
            
            return False

        return check_node(p, q)

        # TC: O(n)
        # SC: O(h)
        # Approach: check for 2 nodes, if both are null then return True. If both are not null then check value. If values are equal, check children. If anything fails return False
        