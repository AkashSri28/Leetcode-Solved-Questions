class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # DP array initialized to 1 because the minimum LIS ending at any element is the element itself
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The result is the maximum value in the dp array
        return max(dp)
    
    # TC: O(n^2)
    #     SC: O(n)
    #         Approach: Find length of longest subsequence ending at i. Return max of all values.
        