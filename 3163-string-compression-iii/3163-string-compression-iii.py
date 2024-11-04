class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        curr = word[0]
        cnt = 1
        for i in range(1, len(word)):
            if curr == word[i] and cnt < 9:
                cnt += 1
            else:
                comp += str(cnt) + curr
                curr = word[i]
                cnt = 1
        
        comp += str(cnt) + curr
        return comp
                
        
#         comp = []
#         i = 0
#         while i < len(word):
#             curr = word[i]
#             j = i
#             while j < len(word) and word[j] == curr and j-i < 9:
#                 j += 1
                
#             comp.append(str(j-i))
#             comp.append(curr)
            
#             i = j
            
#         return ''.join(comp)       
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: Read char from word and count until len is less than 9. Then add to array. Merge array and return.