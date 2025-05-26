class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(colors)
        indegree = [0]*N

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        dp = [[0]*26 for _ in range(N)]
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
                dp[i][ord(colors[i])-ord('a')] = 1
        
        ans = 0
        cnt = 0

        while q:
            n = q.popleft()
            cnt += 1
            ans = max(ans, dp[n][ord(colors[n])-ord('a')])
            for nei in adj[n]:
                for j in range(26):
                    dp[nei][j] = max(dp[nei][j], dp[n][j]+1 if j == (ord(colors[nei])-ord('a')) else dp[n][j])
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if cnt < N:
            return -1
        
        return ans

            
