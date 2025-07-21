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

        # TC: O(n)
        # SC: O(1)
        # Aprroach: tranverse from left to right and for every character check until that char is repeated. When the count is less than 3 add char to ans, else ignore.

        