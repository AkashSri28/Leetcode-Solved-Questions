class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(i):
            nonlocal word_set
            if i < 0:
                return True
            if dp[i] == None:
                dp[i] = False
                for j in range(i, -1, -1):
                    word = s[j:i+1]
                    if word in word_set and helper(j-1):
                        dp[i] = True
                        break
                    
            return dp[i]
           
        n = len(s)
        dp = [None]*(n+1)
        word_set = set(wordDict)
        
        return helper(n-1)
        