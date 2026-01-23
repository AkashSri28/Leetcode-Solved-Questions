class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        freq = dict()
        j = 0
        ans = 0
        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1

            while freq[ch] > 1:
                freq[s[j]] -= 1
                j += 1

            ans = max(ans, i-j+1)

        return ans

        