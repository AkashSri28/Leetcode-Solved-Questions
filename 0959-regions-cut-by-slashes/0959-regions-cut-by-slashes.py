class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        matrix = [[0]*n*3 for _ in range(n*3)]
        regions = 0
        
        def dfs(i, j):
            # print(matrix)
            if i >= 0 and i < n*3 and j >= 0 and j < n*3 and matrix[i][j] == 0:
                matrix[i][j] = 1
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
        
        for i in range(n):
            r = i*3
            for j in range(n):
                c = j*3
                if grid[i][j] == '/':
                    matrix[r][c+2] = matrix[r+1][c+1] = matrix[r+2][c] = 1
                    continue
                if grid[i][j] == '\\':
                    matrix[r][c] = matrix[r+1][c+1] = matrix[r+2][c+2] = 1
                    
        for i in range(n*3):
            for j in range(n*3):
                if matrix[i][j] == 0:
                    regions += 1
                    dfs(i, j)
                    
        return regions
                
    # TC: O(n^2)
    #     SC: O(n^2)
    #         Approach: every cell can be divided into 9 cells. Block cells which are covered by '/' or '\\'. Now use number of islands