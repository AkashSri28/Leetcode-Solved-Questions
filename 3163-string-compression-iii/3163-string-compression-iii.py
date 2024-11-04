class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        while i < len(word):
            curr = word[i]
            j = i
            while j < len(word) and word[j] == curr and j-i < 9:
                j += 1
                
            comp.append(str(j-i))
            comp.append(curr)
            
            i = j
            
        return ''.join(comp)       
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: Read char from word and count until len is less than 9. Then add to array. Merge array and return.