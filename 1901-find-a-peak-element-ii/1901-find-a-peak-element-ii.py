class Solution:
    def findMaxIndex(self, col, mat, m):
        max_ind = 0
        max_val = mat[0][col]
        for i in range(1, m):
            if mat[i][col] > max_val:
                max_val = mat[i][col]
                max_ind = i
        return max_ind


    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        low, high = 0, n-1
        while low <= high:
            mid = (low + high)//2
            max_row = self.findMaxIndex(mid, mat, m)
            if (mid == 0 or mat[max_row][mid] > mat[max_row][mid-1]) and (mid == n-1 or mat[max_row][mid] > mat[max_row][mid+1]):
                return [max_row, mid]
            elif mid > 0 and mat[max_row][mid] < mat[max_row][mid-1]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

        