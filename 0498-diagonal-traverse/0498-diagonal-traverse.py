class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])

        for i in range(m+n-1):
            if i%2 == 0:
                r = min(i, m-1)
                c = i - r
                while r >= 0 and c < n:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(i, n-1)
                r = i - c
                while r < m and c >= 0:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1

        return res

        # TC: O(m**2+n**2)
        # SC: O(1)
        # Approach: i will move from 0 to m+n-1. When i is even, move up, when i is odd move down. Check boundary conditions.

        