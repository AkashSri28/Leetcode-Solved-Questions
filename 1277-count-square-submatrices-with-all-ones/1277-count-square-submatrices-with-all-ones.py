class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        prev = [0]*n
        ans = 0
        
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        curr[j] = 1
                        ans += 1
                        continue
                    curr[j] = 1+min(prev[j-1], prev[j], curr[j-1])
                    ans += curr[j]
            prev = curr
        
        return ans
    
    
    
    # TC: O(m*n)
    #     SC: O(m*n)
    #         Approach: Find number of square matrices ending at (i,j). FInd sum of number of matrices.