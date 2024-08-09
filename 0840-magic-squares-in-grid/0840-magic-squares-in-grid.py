class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        
        def check_square(grid, i, j):
            if row - 1 <= i or i < 1 or col - 1 <= j or j < 1:
                return False
            
            visited = set()
            matrix = []
            for k in range(-1, 2):
                rows = []
                for l in range(-1, 2):
                    if 1 <= grid[i+k][j+l] <= 9 and grid[i+k][j+l] not in visited:
                        visited.add(grid[i+k][j+l])
                        rows.append(grid[i+k][j+l])
                    
                if len(rows) < 3:
                    return False
                matrix.append(rows)
            
            return (matrix[0][0] + matrix[0][1] + matrix[0][2] == 15) and (matrix[1][0] + matrix[1][1] + matrix[1][2] == 15) and (matrix[2][0] + matrix[2][1] + matrix[2][2] == 15) and (matrix[0][0] + matrix[1][0] + matrix[2][0] == 15) and (matrix[0][1] + matrix[1][1] + matrix[2][1] == 15) and (matrix[0][2] + matrix[1][2] + matrix[2][2] == 15) and (matrix[0][0] + matrix[1][1] + matrix[2][2] == 15) and (matrix[0][2] + matrix[1][1] + matrix[2][0] == 15) 
                        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 5:
                    if check_square(grid, i, j):
                        ans += 1
        return ans
    
    # TC: O(r*c)
    #     SC: O(1)
    #         Approach: center element for all such matrices will be 5, check all valid matrices where center is 5
        