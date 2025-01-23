class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [0]*m, [0]*n
        for i in range(m):
            r = 0
            for j in range(n):
                if grid[i][j] == 1:
                    r += 1
            rows[i] = r

        for j in range(n):
            c = 0
            for i in range(m):
                if grid[i][j] == 1:
                    c += 1
            cols[j] = c

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans

        # TC: O(m)+O(n)+O(m*n)
        # SC: O(m+n)
        # Approach: if any row or col has more than 1 computer then computer in that row/ col are connected
                


        