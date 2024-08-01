class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        res = ""
        i, j, flag = 0, 0, True
        
        while i< m and j < n:
            if flag:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            flag = not flag
                
        while i< m:
            res += word1[i]
            i += 1
            
                
        while j < n:
            res += word2[j]
            j += 1
            
        return res
                
        