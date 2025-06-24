class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        temp = [0]*n

        def mark(index):
            left = max(0, index-k)
            right = min(n, index+k+1)
            for i in range(left, right):
                temp[i] = 1

        for index, num in enumerate(nums):
            if num == key:
                mark(index)

        ans = []
        for i in range(n):
            if temp[i] == 1:
                ans.append(i)
        
        return ans