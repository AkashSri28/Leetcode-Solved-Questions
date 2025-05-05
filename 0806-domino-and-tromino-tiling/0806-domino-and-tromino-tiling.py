class Solution:
    def numTilings(self, n: int) -> int:
        dp = [-1]*(n+1)
        mod = 1000000007

        def findCount(n):
            if n < 0:
                return 0
            if n <= 1:
                return 1
            if n == 2:
                return 2
            if dp[n] == -1:
                dp[n] = 2*findCount(n-1) + findCount(n-3)
                dp[n] %= mod
            return dp[n]

        return findCount(n)
        