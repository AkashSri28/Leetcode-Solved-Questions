class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        
        def helper(n):
            if n <= 2:
                return n
            if dp[n] == 0:
                dp[n] = helper(n-1) + helper(n-2)
            return dp[n]
        
        return helper(n)
        