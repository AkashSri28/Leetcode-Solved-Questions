class Solution:
    def minEnd(self, n: int, x: int) -> int:
        curr = x
        i_x = 1
        i_n = 1
        
        while i_n <= n-1:
            if i_x & x == 0:
                if i_n & (n-1):
                    curr = curr | i_x
                i_n = i_n << 1
            i_x = i_x << 1                
            
        return curr
        
        
#         def find_next(c):
#             y = c+1
#             return x|y            
        
#         for _ in range(n-1):
#             curr = find_next(curr)
            
#         return curr
        