class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mem = defaultdict(int)
        maxFreq = 0
        ans = 0

        for r in range(len(s)):
            ch = s[r]
            mem[ch] += 1
            maxFreq = max(maxFreq, mem[ch])

            while r - left + 1 - maxFreq > k:
                mem[s[left]] -= 1
                left += 1

            ans = max(ans, r - left + 1)

        return ans


        