class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sum_digits(s_int):
            res = 0
            while s_int > 0:
                res = res + s_int%10
                s_int //= 10
                
            return res
        
        def char_to_int(ch):
            return ord(ch)-ord('a')+1
        
        s_int = ""
        for ch in s:
            s_int = s_int + str(char_to_int(ch))
            
        s_int = int(s_int)
        
        for i in range(k):
            s_int = sum_digits(s_int)
            
        return s_int
            
        