# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return {}
            if not node.left and not node.right:
                return {1:1}
            
            left_leaf = dfs(node.left)
            right_leaf = dfs(node.right)
            leaf_child = {}
            
            # Count pairs between left and right subtrees
            for d1 in left_leaf:
                for d2 in right_leaf:
                    if d1 + d2 <= distance:
                        res += left_leaf[d1] * right_leaf[d2]
            
            
             # Update the distances for the current node
            for d1 in left_leaf:
                if d1 + 1 in leaf_child:
                    leaf_child[d1 + 1] += left_leaf[d1]
                else:
                    leaf_child[d1 + 1] = left_leaf[d1]
                    
            for d2 in right_leaf:
                if d2 + 1 in leaf_child:
                    leaf_child[d2 + 1] += right_leaf[d2]
                else:
                    leaf_child[d2 + 1] = right_leaf[d2]
            
            return leaf_child
                    
            
        dfs(root)
        return res
        
        