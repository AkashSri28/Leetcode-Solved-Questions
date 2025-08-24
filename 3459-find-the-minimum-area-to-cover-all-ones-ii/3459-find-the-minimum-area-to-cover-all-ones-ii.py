class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def minimumArea(r1, r2, c1, c2, grid):
            minRow, maxRow, minCol, maxCol = float('inf'), -1, float('inf'), -1
            print(r1, r2, c1, c2)
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if grid[i][j] == 1:
                        minRow = min(minRow, i)
                        maxRow = max(maxRow, i)
                        minCol = min(minCol, j)
                        maxCol = max(maxCol, j)
            print(minRow, maxRow, minCol, maxCol)
            if minRow == float('inf'):
                return 0
            return (maxRow - minRow + 1) * (maxCol - minCol + 1)
        
        def gridMinimumArea(grid):
            m, n = len(grid), len(grid[0])
            area = float('inf')
            
            # Split horizontally and vertically
            for i in range(m-1):
                for j in range(n-1):
                    topLeft = minimumArea(0, i, 0, j, grid)
                    topRight = minimumArea(0, i, j+1, n-1, grid)
                    bottom = minimumArea(i+1, m-1, 0, n-1, grid)
                    area = min(area, topLeft + topRight + bottom)
                    # print(topLeft, topRight, bottom)
                    
                    top = minimumArea(0, i, 0, n-1, grid)
                    bottomLeft = minimumArea(i+1, m-1, 0, j, grid)
                    bottomRight = minimumArea(i+1, m-1, j+1, n-1, grid)
                    area = min(area, top + bottomLeft + bottomRight)
                    
            # Split horizontally only
            for i in range(m-2):
                for j in range(i+1, m-1):
                    top = minimumArea(0, i, 0, n-1, grid)
                    middle = minimumArea(i+1, j, 0, n-1, grid)
                    bottom = minimumArea(j+1, m-1, 0, n-1, grid)
                    area = min(area, top + middle + bottom)
                    
            return area
        
        def transpose(grid):
            return [list(row) for row in zip(*grid)]    
        
        area = float('inf')
        area = min(area, gridMinimumArea(grid))
        area = min(area, gridMinimumArea(transpose(grid)))
        return area

        

        