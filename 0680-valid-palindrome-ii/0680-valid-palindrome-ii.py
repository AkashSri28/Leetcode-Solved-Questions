class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return isPalin(l+1, r) or isPalin(l, r-1)
            l += 1
            r -= 1

        return True

        # TC: O(n)
        # SC: O(1)
        # Approach: we will try to check palindrome. If not we can check (i+1, j) and (i, j-1). If any of this is palindrome then we got the answer