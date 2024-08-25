class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [1]*m, [1]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
                    
        for i in range(m):
            for j in range(n):
                if col[j] == 0 or row[i] == 0:
                    matrix[i][j] = 0
                    
                    
        