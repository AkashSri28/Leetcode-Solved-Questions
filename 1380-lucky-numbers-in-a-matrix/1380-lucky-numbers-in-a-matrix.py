class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lucky, min_in_row, max_in_col = [], [0]*m, [0]*n
        
        #store min_in_row
        for i in range(0, m):
            minimum = float('inf')
            for j in range(0, n):
                if matrix[i][j] < minimum:
                    min_in_row[i] = matrix[i][j]
                    minimum = matrix[i][j]
        
        #store max_in_col
        for j in range(0, n):
            maximum = float('-inf')
            for i in range(0, m):
                if matrix[i][j] > maximum:
                    max_in_col[j] = matrix[i][j]
                    maximum = matrix[i][j]
                    
        #check if curr num is lucky number
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == min_in_row[i] and matrix[i][j] == max_in_col[j]:
                    lucky.append(matrix[i][j])        
        
        return lucky
        