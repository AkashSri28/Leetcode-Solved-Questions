class Solution:
    def minChanges(self, s: str) -> int:
        i, ans = 1, 0
        while i < len(s):
            if s[i] != s[i-1]:
                ans += 1
            i += 2
            
        return ans
        