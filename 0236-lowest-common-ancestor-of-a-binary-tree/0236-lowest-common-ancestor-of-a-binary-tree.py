# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def check_node(node, p, q):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = check_node(node.left, p, q)
            right = check_node(node.right, p, q)

            if left and right:
                return node

            if left:
                return left
            return right

        return check_node(root, p, q) 

        # TC: O(n)
        # SC: O(h)
        # Approach: LCA will be one which can target nodes in both of its child. Check for every node and return node if it matches, else return None

            
            

        