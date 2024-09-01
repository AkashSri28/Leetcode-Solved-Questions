class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def func(i, j, k):
            if i == m and j == n and k == l:
                return True
            if (i, j, k) not in dp:
                a = b = False
                if i < m and k < l and s1[i] == s3[k]:
                    a = func(i+1, j, k+1)
                if j < n and k < l and s2[j] == s3[k]:
                    b = func(i, j+1, k+1)
                dp[(i,j,k)] = a or b
                
            return dp[(i,j,k)]
            
        m, n, l = len(s1), len(s2), len(s3)
        dp = dict()
        dp[(m,n,l)] = True
        
        return func(0, 0, 0)
    
    # TC: O(m*n*l)
    #     SC: O(m*n*l)
    #         Approach: dp(i,j,k) represents if we can reach end from i, j, k position.  
        