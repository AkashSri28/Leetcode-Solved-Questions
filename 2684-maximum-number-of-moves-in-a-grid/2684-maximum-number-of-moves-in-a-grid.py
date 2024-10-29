class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]
        # @cache
        # def dp(i, j):
        #     ans = 0
        #     for x, y in dirs:
        #         ni, nj = i + x, j + y
        #         if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:
        #             ans = max(ans, 1 + dp(ni, nj))
        #     return ans
        # return max(dp(i, 0) for i in range(m))
        
        rows, cols = len(grid), len(grid[0])
        dp = [[-1]*cols for _ in range(rows)]
        
        def check(i, j, k, l):
            if k == rows or l == cols or k < 0:
                return 0
            if grid[k][l] > grid[i][j]:
                return 1+calc_moves(k, l)
            return 0
        
        def calc_moves(i, j):
            if i == rows or j == cols or i < 0:
                return 0
            if dp[i][j] == -1:
                top = check(i, j, i-1, j+1)
                right = check(i, j, i, j+1)
                bottom = check(i, j, i+1, j+1)
                dp[i][j] = max(top,right, bottom)               
                
            return dp[i][j]
        
        ans = float('-inf')
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if c == 0:
                    ans = max(ans, calc_moves(r, c))
                
        return ans
        