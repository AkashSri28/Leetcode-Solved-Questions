class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = float('-inf')
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]

        def find_fishes(r, c):
            if r < 0 or c < 0 or r > m-1 or c > n-1 or grid[r][c] == 0 or dp[r][c]!= -1:
                return 0
            if dp[r][c] == -1:
                dp[r][c] = grid[r][c]
                res = 0
                ch = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dx, dy in ch:
                    res += find_fishes(r+dx, c+dy)
                dp[r][c] += res
            return dp[r][c]

        for r in range(m):
            for c in range(n):
                fishes = find_fishes(r, c)
                ans = max(ans, fishes)

        return ans

        # TC: O(m*n)
        # SC: O(m*n)
        # Approach: for each cell check max fishes that can be collected on that cell. Mark cells so path doesnt get repeated

        