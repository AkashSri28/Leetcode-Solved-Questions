class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap = []
        vis = set()
        nei = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(moveTime), len(moveTime[0])

        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        heapq.heappush(heap, (0,0,0,0))
       
        dis = 0

        while heap:
            d, r, c, mov = heapq.heappop(heap)
            vis.add((r, c))

            if r == m-1 and c == n-1:
                return d

            for n1, n2 in nei:
                dr = r+n1
                dc = c+n2

                if dr >= 0 and dr < m and dc >= 0 and dc < n and (dr, dc) not in vis:
                    new_d = max(d, moveTime[dr][dc])
                    v = 0
                    if mov % 2 == 0:
                        v = 1
                    else:
                        v = 2
                    new_d += v

                    if new_d < dp[dr][dc]:
                        dp[dr][dc] = new_d
                        heapq.heappush(heap, (new_d, dr, dc, v))

        return dp[m-1][n-1]

        # TC: O(mnlogmn)
        # SC: O(mn)
        # Approach: Dijkstra with alternate path weight

        