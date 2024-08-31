class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m-1])
        
        dp = [[float("inf")]*n for _ in range(m)]
        
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            
        for i in range(1, m):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                
        return min(dp[m-1])
        