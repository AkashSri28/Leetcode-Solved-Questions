class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[0]*n for _ in range(m)]
        
        for x, y in guards:
            cells[x][y] = 2
            
        for x, y in walls:
            cells[x][y] = 2
            
        def dfs(x, y, dx, dy):
            x = x+dx
            y = y+dy
            while x >= 0 and x < m and y >= 0 and y < n and cells[x][y] != 2:
                cells[x][y] = 1
                x = x+dx
                y = y+dy
            
        for x, y in guards:
            dfs(x, y, -1, 0)
            dfs(x, y, 0, -1)
            dfs(x, y, 1, 0)
            dfs(x, y, 0, 1)
            
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if cells[i][j] == 0:
                    ans += 1
                    
        return ans
        