class Solution:
    def dfs(self, i, j, c, flag, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and flag[i][j] == 0:
            flag[i][j] = c
            self.dfs(i, j+1, c, flag, grid)
            self.dfs(i+1, j, c, flag, grid)
            self.dfs(i, j-1, c, flag, grid)
            self.dfs(i-1, j, c, flag, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        flag = [[0]*n for _ in range(m)]
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and flag[i][j] == 0:
                    cnt += 1
                    self.dfs(i, j, cnt, flag, grid)

        return cnt
        