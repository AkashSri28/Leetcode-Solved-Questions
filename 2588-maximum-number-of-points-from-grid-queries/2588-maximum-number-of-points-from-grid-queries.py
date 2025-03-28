class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        res = [0]*len(queries)
        heap = []
        m, n = len(grid), len(grid[0])
        seen = [[False]*n for _ in range(m)]
        nei = [[0,-1], [0, 1], [-1, 0], [1, 0]]

        heapq.heappush(heap, (grid[0][0], (0,0)))
        seen[0][0] = True
        prev = 0
        for val, idx in sorted_queries:
            while heap and heap[0][0] < val:
                prev += 1
                x, y = heapq.heappop(heap)[1]
                for dx, dy in nei:
                    x1, y1 = x+dx, y+dy
                    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and not seen[x1][y1]:
                        heapq.heappush(heap, (grid[x1][y1], (x1, y1)))
                        seen[x1][y1] = True
            res[idx] = prev

        return res

        # TC: O(klogk + m*nlogm*n)
        # SC: O(m*n)
        # Approach:we can find what numbers are than current query value and keep increase cnt



        