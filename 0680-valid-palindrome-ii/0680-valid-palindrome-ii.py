class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while l <= r:
            if s[l] != s[r]:
                return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
            l += 1
            r -= 1
        return True

# TC: O(n)
# SC: O(1)
# Clarification: can clarify if its char string
# Brute Force: check string for palindrome by removing 1 char everytime, O(n**2)
# Approach: we will use palindrome logic, whenever there is mismatch we will check both possibilities l+1, r and l, r-1
# Testing: check for "", "abbab", "abbca", "abbbb"


            
        