class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        j = ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans += (i-j)
                s[i], s[j] = s[j], s[i]
                j += 1
                
        return ans