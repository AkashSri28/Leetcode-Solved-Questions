"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, node, ans):
        if not node:
            return
        for child in node.children:
            self.helper(child, ans)
        ans.append(node.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.helper(root, ans)
        
        return ans