class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return True
            if rank[pu] > rank[pv]:
                parent[pv] = pu
                rank[pu] += pv
            else:
                parent[pu] = pv
                rank[pv] += pu
            return False

        for u, v in edges:
            if union(u, v):
                return [u, v]

        # TC: O(E+V)
        # SC: O(E)
        # Approach: try to find parent for all nodes, if there is a loop parent of the node will already exist.


        