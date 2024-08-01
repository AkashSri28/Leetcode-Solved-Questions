class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        count = 0
        
        def bfs(grid, i, j):
            nonlocal m, n, visited
            if i < 0 or j <0 or i>=m or j >= n or grid[i][j] == "0" or visited[i][j]:
                return
            visited[i][j] = True
            bfs(grid, i-1, j)
            bfs(grid, i, j-1)
            bfs(grid, i+1, j)
            bfs(grid, i, j+1)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visited[i][j]:
                    continue
                count += 1
                bfs(grid, i, j)
                
        return count
        