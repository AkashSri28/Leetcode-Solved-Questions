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

        # TC: O(n)
        # SC: O(n)
        # Approach: Find length of longest valid paranthesis ending at index i. So we will check only if i has ')'.
        # Now if i-1 is '(', we will find dp[i-2]+2        ....()
        # else if i-1 is ')'
        # then there will be 2 cases
        #     ....(()) or ....)())
        #     so we will check at dp[i-1-dp[i-1]] if that is ( then we will check 2+dp[i-1]+dp[i-2-dp[i-1]]