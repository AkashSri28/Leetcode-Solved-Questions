class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = ""
        while i < n:
            j = i
            cnt = 1
            while j < n and s[j] == s[i]:
                if cnt < 3:
                    ans += s[j]
                    cnt += 1
                j += 1
            i = j
        return ans

        # TC: O(n)
        # SC: O(1)
        # Aprroach: tranverse from left to right and for every character check until that char is repeated. When the count is less than 3 add char to ans, else ignore.

        