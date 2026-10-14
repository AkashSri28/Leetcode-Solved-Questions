class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            mid = matrix[i][j]
            if mid == target:
                return True
            elif mid < target:
                i += 1
            else:
                j -= 1
            
        return False
        
# Clarification: clarify range of m and n
# Brute Force: check linearly in each row
# Approach: for each we will apply binary search
# TC: O(m*logn)
# SC: O(1)
# Testing: