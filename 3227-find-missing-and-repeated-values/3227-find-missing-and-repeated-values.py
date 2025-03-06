class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        mem = [0]*(n**2+1)
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                mem[num] += 1

        ans = [0]*2
        for i in range(1, n**2+1):
            if mem[i] == 1:
                continue
            elif mem[i] == 2:
                ans[0] = i
            else:
                ans[1] = i

        return ans

        # TC: O(n**2)
        # SC: O(n**2)
        # Approach: count occurance to find missing and duplicate number
            

        