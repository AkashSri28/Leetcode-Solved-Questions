class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = []
        while i < n:
            j = i
            cnt = 0
            while j < n and s[j] == s[i]:
                if cnt < 2:
                    ans.append(s[j])
                    cnt += 1
                j += 1
            i = j
        return ''.join(ans)

        