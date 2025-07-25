class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        seen = set()
        for num in nums:
            if num not in seen and num > 0:
                res += num
                seen.add(num)

        if res == 0:
            res = max(nums)
        return res
        