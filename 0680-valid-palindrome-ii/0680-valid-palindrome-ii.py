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