class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            # If the current cell is out of bounds or water in grid2, return True
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True

            # Mark the current cell as visited in grid2
            grid2[i][j] = 0

            # Check if this cell in grid2 corresponds to land in grid1
            is_sub_island = grid1[i][j] == 1

            # Explore all four directions and check if they are part of the sub-island
            is_sub_island &= dfs(i-1, j)
            is_sub_island &= dfs(i+1, j)
            is_sub_island &= dfs(i, j-1)
            is_sub_island &= dfs(i, j+1)

            return is_sub_island

        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:  # Start DFS if we find land in grid2
                    if dfs(i, j):  # Check if this island is a sub-island
                        count += 1

        return count


        