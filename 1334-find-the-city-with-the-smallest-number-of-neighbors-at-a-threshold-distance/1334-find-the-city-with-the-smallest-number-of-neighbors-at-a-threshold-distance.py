class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, dist in edges:
            graph[u].append([v, dist])
            graph[v].append([u, dist])
            
        def dijkstra(src):
            heap = [[0, src]]
            visited = set()
            
            while heap:
                dist, node = heapq.heappop(heap)
                if node not in visited:
                    visited.add(node)
                    for nei, nei_dist in graph[node]:
                        if nei_dist+dist <= distanceThreshold:
                            heapq.heappush(heap, [nei_dist+dist, nei])
            
            return len(visited) - 1
            
        
        res, min_nei = 0, 101
        
        for i in range(n):
            nei_cnt = dijkstra(i)
            if nei_cnt <= min_nei:
                min_nei = nei_cnt
                res = i
        
        return res
        