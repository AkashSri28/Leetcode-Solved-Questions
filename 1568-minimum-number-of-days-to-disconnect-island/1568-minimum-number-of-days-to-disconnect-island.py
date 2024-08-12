class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])       
        
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0 or visited[i][j]:
                return 
            visited[i][j] = True
            dfs(i+1, j, visited)
            dfs(i, j+1, visited)
            dfs(i-1, j, visited)
            dfs(i, j-1, visited)
            
        def count_num_islands():
            num_islands = 0
            visited = [[False]*COLS for _ in range(ROWS)]
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1 and not visited[i][j]:
                        num_islands += 1
                        dfs(i, j, visited)          
                        
            return num_islands
        
                    
        if count_num_islands() != 1:
            return 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_num_islands() != 1:
                        return 1                    
                    grid[i][j] = 1
        
        return 2
                    
    # TC: O(m*n)^2
    #     SC:(m*n)    #visited[][]
    #         Approach: count number of islands. if num is anything except 1, we can return 0. At max answer can be 2. So try to remove 1 land and check if get any ans, else ans is 2
    #         Learning: Look at constraints to get idea on brute force