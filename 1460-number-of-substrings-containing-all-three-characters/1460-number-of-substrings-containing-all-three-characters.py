class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        ans = 0
        mem = defaultdict(int)

        for r in range(len(s)):
            ch = s[r]
            mem[ch] += 1
            while len(mem) == 3:
                ans += (len(s) - r)
                ch2 = s[l]
                mem[ch2] -= 1
                if mem[ch2] == 0:
                    mem.pop(ch2)
                l += 1

        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: Use sliding window to count atleast 1 occurance of abc. Find all strings which satisfy this and update l.
        