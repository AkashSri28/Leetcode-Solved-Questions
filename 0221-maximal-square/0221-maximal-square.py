class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        max_sq = 0
        
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == "1"):
                    if(i == 0 or j == 0):
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    max_sq = max(max_sq, dp[i][j])
        return max_sq**2           
                
        