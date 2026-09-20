class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1

        while low <= high:
            mid = (low + high)// 2
            i = mid // n
            j = mid % n
            num = matrix[i][j]

            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
        
# TC: O(logM*N)
# SC: O(1)
# Approach: Instead of check all elements one by one, we can use binary search to to find element