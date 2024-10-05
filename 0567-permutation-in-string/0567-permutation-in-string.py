class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        
        if s1_len > s2_len:
            return False
        
        count_s1 = [0]*26
        count_s2 = [0]*26
        
        for ch in s1:
            count_s1[ord(ch)-ord('a')] += 1
            
        for i in range(len(s1)):
            count_s2[ord(s2[i]) - ord('a')] += 1
            
        if tuple(count_s2) == tuple(count_s1):
            return True
        
        i, j = 0, len(s1)
        
        while j < len(s2):
            count_s2[ord(s2[j]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] -= 1
            
            if tuple(count_s2) == tuple(count_s1):
                return True
            
            i += 1
            j += 1
            
        return False
        