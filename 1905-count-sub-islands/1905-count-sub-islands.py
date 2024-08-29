class Solution:
    def dfs(self, grid2, i, j, grid1, m, n, vis):
        if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0 or vis[i][j] == 1:
                return True
            
        vis[i][j] = 1
        res = True
        if grid1[i][j] == 0:
            res = False
        return res & self.dfs(grid2, i+1, j, grid1, m, n, vis) & self.dfs(grid2, i, j-1, grid1, m, n, vis) & self.dfs(grid2, i-1, j, grid1, m, n, vis) & self.dfs(grid2, i, j+1, grid1, m, n, vis)

        
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, cnt = len(grid2), len(grid2[0]), 0
        vis = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and vis[i][j] == 0 and self.dfs(grid2, i, j, grid1, m, n, vis):
                    cnt += 1
                        
        return cnt
        