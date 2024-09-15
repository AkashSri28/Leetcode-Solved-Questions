class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = 0
        state = {0: -1}
        ans = 0
        vowels = {
            'a':0,
            'e':1,
            'i':2,
            'o':3,
            'u':4
            }
        
        for i, ch in enumerate(s):
            if ch in vowels:
                bit = vowels[ch]
                bitmask = bitmask^(1<<bit)
                
            if bitmask in state:
                ans = max(ans, i-state[bitmask])
            else:
                state[bitmask] = i
                
        return ans
            
        