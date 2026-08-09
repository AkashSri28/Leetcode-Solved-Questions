class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mem = defaultdict(int)
        ans = 0
        for r in range(len(s)):
            ch = s[r]
            mem[ch] += 1
            while mem[ch] > 1:
                mem[s[left]] -= 1
                left += 1
            ans = max(ans, r - left + 1)
        
        return ans

# TC: O(n)
# SC: O(1)
# Clarification: 
# Brute Force:
# Approach: 
# Testing: