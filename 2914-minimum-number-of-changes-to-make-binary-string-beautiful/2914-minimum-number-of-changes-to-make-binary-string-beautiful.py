class Solution:
    def minChanges(self, s: str) -> int:
        i, ans = 1, 0
        while i < len(s):
            if s[i] != s[i-1]:
                ans += 1
            i += 2
            
        return ans
    
    # TC: O(n)    n: len(s)
    #         SC: O(1)
    #             Approach: to get all even length substrings, check if all substrings have same char, change any one if chars are not same
        