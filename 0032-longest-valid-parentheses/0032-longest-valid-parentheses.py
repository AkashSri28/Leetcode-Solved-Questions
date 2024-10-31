class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        ans = 0
        
        def helper(i):
            if i <= 0:
                return 0
            if s[i-1] == '(':
                dp[i] = 2+dp[i-2] if i-2 >= 0 else 2 
            else:
                length = dp[i-1]
                if length == 0:
                    return 0
                if i-length-1 >= 0 and s[i-length-1] == '(':
                    dp[i] = 2+length+dp[i-length-2]
            return dp[i]
            
        for index, ch in enumerate(s):
            if ch == ')':
                ans = max(ans, helper(index))
                
        return ans
            
                