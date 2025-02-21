# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def backtrack(self, node, parent, isLeft):
        if node:
            nodeVal = 2*parent+1
            if not isLeft:
                nodeVal += 1
            self.mem.add(nodeVal)
            self.backtrack(node.left, nodeVal, True)
            self.backtrack(node.right, nodeVal, False)


    def __init__(self, root: Optional[TreeNode]):
        self.mem = set()
        if root:
            self.mem.add(0)
            self.backtrack(root.left, 0, True)
            self.backtrack(root.right, 0, False)

        

    def find(self, target: int) -> bool:
        return target in self.mem

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)