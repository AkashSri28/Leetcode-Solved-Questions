class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        res = 0
                
        def postOrder(node, parent):
            nonlocal res
            total = 0
            for child in adj[node]:
                if child != parent:
                    total += postOrder(child, node)
                    
            total += values[node]
            if total % k == 0:
                res += 1
                
            return total
                
        postOrder(0, -1)
        return res
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: for each node check if its value is divisible by k
            
            
        
        