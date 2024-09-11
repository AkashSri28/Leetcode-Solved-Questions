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
    
    # TC: O(log n, base 2)    #n is xor of 2 numbers
    #     SC: O(1)
    #         Approach: XOR sets the bits which are different in 2 numbers. Find XOR and count bits in XOR.
        