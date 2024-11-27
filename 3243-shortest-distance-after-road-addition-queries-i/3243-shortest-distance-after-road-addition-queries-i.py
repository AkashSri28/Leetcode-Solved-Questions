class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(n-1):
            adj[i].append(i+1)
        
        ans = []
        
        def bfs(query):
            u, v = query
            adj[u].append(v)
            queue = deque()
            visited = [-1]*n
            queue.append((0, 0))
            while queue:
                node, dis = queue.popleft()
                if visited[node] == -1:
                    visited[node] = dis
                    for nei in adj[node]:
                        queue.append((nei, dis+1))
                            
                        
            return visited[n-1]
                    
                
        for query in queries:
            ans.append(bfs(query))
            
        return ans
            