# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ans = set()
        ans.add(root)
        
        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in to_delete:
                if node in ans:
                    ans.remove(node)
                if node.left:
                    ans.add(node.left)
                if node.right:
                    ans.add(node.right)
                res = None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res
                
        
        dfs(root)
        
        return list(ans)
        