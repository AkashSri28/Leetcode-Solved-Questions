class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        chars = list(s)
        cnt = 0
        for ch in s:
            if ch in vowels:
                cnt += 1
                return True
        return False