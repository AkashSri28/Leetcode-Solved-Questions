# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        split = re.findall(r'-*\d+', traversal)

        stack = []
        if not split:
            return None

        for item in split:
            depth = item.count('-')
            val = int(item.lstrip('-'))

            node = TreeNode(val)
            if stack:
                if len(stack) == depth:
                    stack[-1].left = node
                else:
                    while len(stack) > depth:
                        stack.pop()
                    stack[-1].right = node

            stack.append(node)

        return stack[0]

        