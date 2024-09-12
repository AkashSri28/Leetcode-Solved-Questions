class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_mask = 0
        for ch in allowed:
            bit = 1<<(ord(ch)-ord('a'))
            allowed_mask = allowed_mask|bit
            
        ans = len(words)
        for word in words:
            for ch in word:
                bit = 1<<(ord(ch)-ord('a'))
                res = allowed_mask & bit
                if res == 0:
                    ans -= 1
                    break
                    
        return ans
        
#         allowed_set = set(allowed)
#         ans = 0
#         for word in words:
#             cnt = 0
#             for i in range(len(word)):
#                 if word[i] not in allowed_set:
#                     break
#                 cnt += 1
#             if cnt == len(word):
#                 ans += 1
                
#         return ans
        
        