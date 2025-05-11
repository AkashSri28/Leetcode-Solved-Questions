class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = dict()
        dp[(m,n)] = True

        def match(i, j):
            if (i, j) not in dp:
                if i == m:
                    if p[j] == '*':
                        dp[(i, j)] = match(i, j+1)
                    else:
                        dp[(i, j)] = False
                elif j == n:
                    dp[(i, j)] = False
                else:
                    if p[j] == '?':
                        dp[(i, j)] = match(i+1, j+1)
                    elif p[j] == '*':
                        dp[(i, j)] = match(i, j+1) | match(i+1, j+1) | match(i+1, j)
                    else:
                        if s[i] == p[j]:
                            dp[(i, j)] = match(i+1, j+1)
                        else:
                            dp[(i, j)] = False                

            return dp[(i, j)]

        return match(0, 0)