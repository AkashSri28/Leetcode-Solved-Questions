class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        for ch in s:
            if ch in vowels:
                return True
        return False