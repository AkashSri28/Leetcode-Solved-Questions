class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def func(i, j):
            if i == m-1 and j == n-1 and obstacleGrid[i][j] != 1:
                return 1
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            if dp[i][j] == -1:
                dp[i][j] = func(i+1, j) + func(i, j+1)
            
            return dp[i][j]
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        
        return func(0, 0)
        