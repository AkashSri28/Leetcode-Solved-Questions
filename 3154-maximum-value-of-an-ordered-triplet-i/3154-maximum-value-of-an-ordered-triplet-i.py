class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        i = 0

        for j in range(i+1, n-1):
            if nums[j] > nums[i]:
                i = j
                continue
            for k in range(j+1, n):
                a = (nums[i] - nums[j])*nums[k]
                res = max(res, a)

        return res
        