class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def func(i, j):
            if dp[i][j] == None:
                if word1[i] != word2[j]:
                    dp[i][j] = 1+min(func(i+1, j+1), func(i+1, j), func(i, j+1))
                else:
                    dp[i][j] = func(i+1, j+1)
            return dp[i][j]
        
        m, n = len(word1), len(word2) 
        dp = [[None]*(n+1) for _ in range(m+1)]
        
        dp[m][n] = 0
        for i in range(m-1, -1, -1):
            dp[i][n] = dp[i+1][n]+1
            
        for i in range(n-1, -1, -1):
            dp[m][i] = dp[m][i+1]+1
            
        return func(0, 0)
        