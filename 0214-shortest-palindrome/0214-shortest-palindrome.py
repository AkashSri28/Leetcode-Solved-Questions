class Solution:
    
    def shortestPalindrome(self, s: str) -> str:
        
        #find longest palindrome starting at 0
        if len(s) == 0:
            return ""
        
        prefix = suffix = 0
        base = 29
        power = 1
        
        for i, c in enumerate(s):
            val = ord(c) - ord('a')
            prefix *= 29
            prefix += val
            
            suffix += (val*power)
            power *= 29
            
            if prefix == suffix:
                index = i
                
        rem = s[index+1:][::-1]
        return rem+s
            
        
        