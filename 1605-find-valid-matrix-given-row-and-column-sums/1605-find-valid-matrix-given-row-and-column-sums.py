class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        
        matrix = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        
        return matrix
        
# TC: O(m*n)
# SC: O(m*n) for storing result
# Approach: at any position, value will be minimum of possible rowSum and colSum