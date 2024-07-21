class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0]*k for _ in range(k)]
        
        def topo_sort(edges):
            graph = defaultdict(list)
            in_degree = {i:0 for i in range(1, k+1)}
            order_list = []
            
            for u,v in edges:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([i for i in range(1, k+1) if in_degree[i] == 0])
            
            while queue:
                node = queue.popleft()
                order_list.append(node)
                
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)
                        
            return order_list                                
        
        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        
        if len(row_order) < k or len(col_order) < k:
            return []
        
        row_position = {n:i for i,n in enumerate(row_order)}
        col_position = {n:i for i,n in enumerate(col_order)}
        
        for i in range(1, k+1):
            matrix[row_position[i]][col_position[i]] = i
        
        return matrix
    
# TC: O(m+n+k)    
#     creating graph: O(n) and O(m) -> O(m+n)
#     creating topo sort: number of edges: O(V+E): O(k+m+n)
#     creating matrix: O(k)
        
# SC: O(m+n)  graph
#     O(k)    order_list
#     O(k^2)  matrix
#     O(m+n+k^2) overall
    
# Approach: which node will come first will be determined using topo sort
#     if topo sort is less than k, means all nodes are not covered, return empty array
#     if there is result, generate final position for each num using row and col indexes
