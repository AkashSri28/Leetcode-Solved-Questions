class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        sq_cnt = [[0]*n for _ in range(m)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    sq_cnt[i][j] = matrix[i][j]
                    ans += sq_cnt[i][j]
                    continue
                if matrix[i][j] == 1:
                    sq_cnt[i][j] = 1+min(sq_cnt[i-1][j-1], sq_cnt[i-1][j], sq_cnt[i][j-1])
                    ans += sq_cnt[i][j]
        
        return ans