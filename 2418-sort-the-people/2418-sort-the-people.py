class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        res = []
        for i in range(n):
            res.append([heights[i], names[i]])
        res.sort(reverse = True)
        return [name for height, name in res]
        