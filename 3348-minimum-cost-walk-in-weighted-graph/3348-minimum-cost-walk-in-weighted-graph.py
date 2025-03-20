class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        compId = [0]*n
        adj = defaultdict(list)
        compWt = dict()
        ans = []

        for u, v, wt in edges:
            adj[u].append(v)
            adj[v].append(u)

        def findCompId(i, id):
            compId[i] = id
            for nei in adj[i]:
                if compId[nei] == 0:
                    findCompId(nei, id)
            
        id = 1
        for i in range(n):
            if compId[i] == 0:
                findCompId(i, id)
                id += 1

        for u, v, wt in edges:
            cU = compId[u]
            if cU not in compWt:
                compWt[cU] = 2**31-1
            compWt[cU] &= wt

        for u, v in query:
            if compId[u] != compId[v]:
                ans.append(-1)
            else:
                ans.append(compWt[compId[u]])
        
        return ans


        
        