class Solution:
    def reverse(self, x: int) -> int:
        flag, ans = 1, 0
        if x < 0:
            flag = -1
            x = abs(x)
            
        while x > 0:
            ans = ans*10 + (x % 10)
            x = x // 10
            
        ans *= flag
        
        if ans <= (-2)**(31) or ans >= 2**(31) - 1:
            return 0
        return ans
        