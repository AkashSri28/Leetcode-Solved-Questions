class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        mem = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

        def find_MD():
            return abs(mem['N']-mem['S']) + abs(mem['E']-mem['W'])

        for i in range(len(s)):
            ch = s[i]
            mem[ch] += 1
            md = find_MD()
            steps = i+1

            if steps > md:
                diff = steps-md
                add = min(2*k, diff)
                md = md+add

            ans = max(ans, md)

        return ans


        

        