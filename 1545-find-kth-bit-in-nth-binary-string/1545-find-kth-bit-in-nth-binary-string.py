class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        
        while len(s) < k:
            s = s+'1'
            j = len(s) - 2
            while j >= 0:
                if s[j] == '1':
                    s = s+'0'
                else:
                    s = s+'1'
                j -= 1
                
        return s[k-1]
        