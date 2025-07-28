class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)
        for num in nums:
            max_or |= num

        def dp(index, curr):
            if index == n:
                return 1 if curr == max_or else 0
            return dp(index+1, curr) + dp(index+1, curr|nums[index])

        return dp(0,0)


        