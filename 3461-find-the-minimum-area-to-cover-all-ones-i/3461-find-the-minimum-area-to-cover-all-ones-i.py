class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        def first_last_one(arr):
            first = -1
            last = -1

            for i, val in enumerate(arr):
                if val == 1:
                    if first == -1:  
                        first = i
                    last = i          

            return last - first + 1
        
        r, c = len(grid), len(grid[0])
        rows = [0]*r
        cols = [0]*c

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rows[i] = 1
                    cols[j] = 1
        
        l = first_last_one(rows)
        b = first_last_one(cols)
        return l*b

        




        