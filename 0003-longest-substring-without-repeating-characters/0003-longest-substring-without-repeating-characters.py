class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        j = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch in last and last[ch] >= j:
                j = last[ch] + 1
            last[ch] = i
            ans = max(ans, i-j+1)

        return ans

        # TC: O(n)
        # SC: O(characters)
        # Approach: store last index of character seen, if its greater than j, then move j to ch+1 to avoid duplicate

        