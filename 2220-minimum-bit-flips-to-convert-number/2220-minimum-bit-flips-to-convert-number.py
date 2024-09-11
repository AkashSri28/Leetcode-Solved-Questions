class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def count_bits(n):
            ans = 0
            while n > 0:
                ans += n%2
                n //= 2
                
            return ans    
                
        xor = start^goal
        return count_bits(xor)
        