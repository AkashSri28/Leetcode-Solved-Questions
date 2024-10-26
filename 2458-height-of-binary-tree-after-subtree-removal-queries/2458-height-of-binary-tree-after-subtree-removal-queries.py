# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_depth = defaultdict(int)
        node_height = defaultdict(int)
        
        def dfs(node, lvl):
            if not node:
                return -1
            node_height[node.val] = lvl
            left = dfs(node.left, lvl + 1)
            right = dfs(node.right, lvl + 1)
            node_depth[node.val] = 1+max(left, right)
            return node_depth[node.val]
        
        dfs(root, 0)
        
        max_height = node_height[root.val] + node_depth[root.val]
        
        height_dict = defaultdict(list)
        for node, height in node_height.items():
            values = height_dict[height]
            ht = node_height[node] + node_depth[node]
            values.append(ht)
            values.sort(reverse=True)
            if len(values) > 2:
                values.pop()
            height_dict[height] = values
                
        
        ans = []
        for q in queries:
            lvl = node_height[q]
            height = lvl + node_depth[q]
            if height != max_height:
                ans.append(max_height)
                continue
            values = height_dict[lvl]
            if len(values) == 2:
                ans.append(values[1])
            else:
                ans.append(lvl-1)
                
        return ans
                
            
            
                
                