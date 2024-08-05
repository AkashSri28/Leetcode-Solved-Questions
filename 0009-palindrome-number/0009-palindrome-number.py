class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse, copy = 0, x
        
        while copy > 0:
            reverse = reverse*10 + (copy % 10)
            copy = copy // 10
            
        if reverse == x:
            return True
        return False
        