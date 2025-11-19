# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.ls = self._flatten(nestedList)
    
    def next(self) -> int:
        val = self.ls[self.idx]
        self.idx += 1
        return val 
    
    def hasNext(self) -> bool:
        return self.idx < len(self.ls)

    def _flatten(self, arr):
        res = []
        for ni in arr:
            if ni.isInteger():
                res.append(ni.getInteger())
            else:
                res.extend(self._flatten(ni.getList()))
        return res

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())