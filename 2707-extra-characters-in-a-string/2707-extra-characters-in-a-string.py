class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)  # Convert the dictionary to a set for fast lookup
        
        # dp[i] will represent the minimum extra characters in the substring s[i:]
        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # Base case: no extra characters when the string is empty
        
        # Traverse the string from the end to the start
        for i in range(n - 1, -1, -1):
            # By default, treat the current character as extra
            dp[i] = dp[i + 1] + 1
            
            # Try to match any word in the dictionary starting at index i
            for length in range(1, n - i + 1):
                if s[i:i + length] in word_set:
                    dp[i] = min(dp[i], dp[i + length])
        
        return dp[0]
        