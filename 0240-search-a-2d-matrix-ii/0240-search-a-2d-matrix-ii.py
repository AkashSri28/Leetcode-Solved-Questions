class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            low, high = 0, n-1
            while low <= high:
                mid = (low + high)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    low = mid+1
                else:
                    high = mid-1

        return False
        