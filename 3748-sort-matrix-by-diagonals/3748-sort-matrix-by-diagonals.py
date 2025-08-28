class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        g = [row[:] for row in grid]  # copy to avoid mutating input

        # helper: collect a diagonal starting at (r, c), sort, and write back
        def process_diag(r, c, reverse: bool):
            i, j = r, c
            buf = []
            while i < n and j < n:
                buf.append(g[i][j])
                i += 1; j += 1
            buf.sort(reverse=reverse)
            i, j = r, c
            k = 0
            while i < n and j < n:
                g[i][j] = buf[k]
                i += 1; j += 1
                k += 1

        # Bottom-left triangle (including main diagonal): start from first column
        # and sort each diagonal in non-increasing order.
        for r in range(n):
            process_diag(r, 0, reverse=True)   # descending

        # Top-right triangle: start from first row (skip (0,0) to avoid redoing main diag)
        # and sort each diagonal in non-decreasing order.
        for c in range(1, n):
            process_diag(0, c, reverse=False)  # ascending

        return g
                
                
        