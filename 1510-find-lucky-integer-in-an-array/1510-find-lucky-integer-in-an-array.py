class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mem = Counter(arr)
        ans = -1
        for k, v in mem.items():
            if k == v and k > ans:
                ans = k

        return ans
        