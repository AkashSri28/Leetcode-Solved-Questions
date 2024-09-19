class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[float('-inf')] * (n + 1) for _ in range(5)]

        for j in range(n + 1):
            dp[0][j] = 0

        for i1 in range(1, 5):
            for i2 in range(1, n + 1):
                take = dp[i1 - 1][i2 - 1] + a[i1 - 1] * b[i2 - 1]
                not_take = dp[i1][i2 - 1]
                dp[i1][i2] = max(take, not_take)

        return dp[4][n]
        
        
#         m, n = len(b), len(a)
#         dp = [[-float('inf')]*n for _ in range(m)]

#         def func(i, j):
#             if j == n:
#                 return 0
#             if i == m:
#                 return -(10**6)
            
#             if dp[i][j] == -float('inf'):
#                 dp[i][j] = b[i]*a[j] + func(i+1, j+1)
#                 if i<m:
#                     dp[i][j] = max(dp[i][j], func(i+1, j))

#             return dp[i][j]

#         return func(0, 0)
        