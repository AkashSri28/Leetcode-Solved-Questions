class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, i):
            nonlocal dp
            if i < 0:
                return 0
            if dp[i] == -1:
                dp[i] = max(nums[i] + helper(nums, i-2), helper(nums, i-1))
                
            return dp[i]            
        
        n = len(nums)
        dp = [-1]*n
        
        return helper(nums, n-1)
        