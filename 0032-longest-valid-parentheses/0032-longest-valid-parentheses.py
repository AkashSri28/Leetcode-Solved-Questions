class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        ans = 0

        for i in range(n):
            if s[i] == ')':
                if i-1 >= 0 and s[i-1] == '(':
                    dp[i] = 2+dp[i-2]
                else:
                    if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                        dp[i] = 2+dp[i-1]+(dp[i-2-dp[i-1]])

                ans = max(ans, dp[i])
        return ans