class Solution:        
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[float("inf")]*n for _ in range(m)]
        vis = [[0]*n for _ in range(m)]
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])
                    res[i][j] = 0
                    vis[i][j] = 1
                    
        while queue:
            i, j , distance = queue.popleft()
            if i-1 >= 0 and vis[i-1][j] == 0:
                queue.append([i-1, j, distance+1])
                res[i-1][j] = 1+distance
                vis[i-1][j] = 1
                
            if j+1 < n and vis[i][j+1] == 0:
                queue.append([i, j+1, distance+1])
                res[i][j+1] = 1+distance
                vis[i][j+1] = 1
                
            if i+1 < m and vis[i+1][j] == 0:
                queue.append([i+1, j, distance+1])
                res[i+1][j] = 1+distance
                vis[i+1][j] = 1
                
            if j-1 >= 0 and vis[i][j-1] == 0:
                queue.append([i, j-1, distance+1])
                res[i][j-1] = 1+distance
                vis[i][j-1] = 1
                
                    
        return res
        