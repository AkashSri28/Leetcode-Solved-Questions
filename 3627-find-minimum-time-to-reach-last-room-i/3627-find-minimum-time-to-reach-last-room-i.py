class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        vis = set()

        heap = [(0, 0, 0)]
        vis.add((0, 0))
        nei = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while heap:
            dis, r , c = heapq.heappop(heap)
            if (r == m-1 and c == n-1):
                return dis
            
            for n1, n2 in nei:
                dr, dc = r+n1, c+n2

                if dr >= 0 and dr < m and dc >= 0 and dc < n and (dr, dc) not in vis:
                    vis.add((dr, dc))
                    new_dis = max(dis, moveTime[dr][dc]) + 1
                    if res[dr][dc] > new_dis:
                        res[dr][dc] = new_dis
                        heapq.heappush(heap, (new_dis, dr, dc))

        return res[m-1][n-1]
