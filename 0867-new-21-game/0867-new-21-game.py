class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = dict()
        window_sum = 0
        for i in range(k, k+maxPts):
            if i <= n:
                dp[i] = 1
                window_sum += 1
            else:
                dp[i] = 0

        for i in range(k-1, -1, -1):
            dp[i] = window_sum/maxPts
            window_sum = window_sum + dp[i] - dp[i+maxPts]

        return dp[0]
        