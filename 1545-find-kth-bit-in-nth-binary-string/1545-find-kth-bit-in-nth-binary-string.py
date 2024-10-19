class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def flip(n):
            if n == '1':
                return '0'
            return '1'
        
        def helper(n, k):
            if n == 1:
                return '0'
            
            len_s = 2**n - 1
            mid = len_s//2 + 1
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n-1, k)
            else:
                return flip(helper(n-1, 1+(len_s)-k))
            
                
        
        return helper(n, k)
        
        
#         if k == 1:
#             return '0'
        
#         s = '0'
        
#         while len(s) < k:
#             s = s+'1'
#             j = len(s) - 2
#             while j >= 0:
#                 if s[j] == '1':
#                     s = s+'0'
#                 else:
#                     s = s+'1'
#                 j -= 1
                
#         return s[k-1]
    
    # TC: O(k**2)
    #     SC: O(k)
        