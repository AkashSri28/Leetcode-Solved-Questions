class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        new_s = ""
        for i in range(n):
            if i >= 2 and s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            new_s = new_s + s[i]
        return new_s
        