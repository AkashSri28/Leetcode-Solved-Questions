class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_r = zero_c = False
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            if matrix[r][0] == 0:
                zero_c = True
                break

        for c in range(n):
            if matrix[0][c] == 0:
                zero_r = True
                break

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0

        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0

        if zero_r:
            for c in range(n):
                matrix[0][c] = 0

        if zero_c:
            for r in range(m):
                matrix[r][0] = 0

        # TC: O(mn)
        # SC: O(1)
        # Approach: Use 1st row and 1st column to store if all values in that row/ column will be 0. For (0,0) use a seperate variable        