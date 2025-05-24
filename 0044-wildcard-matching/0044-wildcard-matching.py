class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[-1]*(m+1) for _ in range(n+1)]

        def match(i, j):
            if i == n and j == m:
                return True
            if i == n:
                return False
            if j == m:
                # Remaining pattern must be all '*'
                return all(x == '*' for x in p[i:])
            if dp[i][j] == -1:
                if p[i] == '*':
                    dp[i][j] = match(i+1, j)|match(i+1, j+1)|match(i, j+1)
                elif p[i] == '?' or p[i] == s[j]:
                    dp[i][j] = match(i+1, j+1)
                else:
                    dp[i][j] = False
            return dp[i][j]

        return match(0, 0)

        # TC: O(m*n)
        # SC: O(m*n)
        # Approach: every state (i, j) tells if [0..i] and [0..j] matches