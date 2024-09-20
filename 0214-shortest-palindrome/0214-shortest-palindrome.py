class Solution:
    
    def shortestPalindrome(self, s: str) -> str:
        
        #find longest palindrome starting at 0        
        prefix = suffix = 0
        base = 26
        power = 1
        index = 0
        mod = 10**9 + 7
        
        for i, c in enumerate(s):
            val = (ord(c) - ord('a')+1)
            prefix *= base
            prefix += val
            prefix %= mod
            
            suffix += (val*power)
            power *= base
            suffix %= mod
            
            if prefix == suffix:
                index = i
                
        rem = s[index+1:][::-1]
        return rem+s
            
        
        