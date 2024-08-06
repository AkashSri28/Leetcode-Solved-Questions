class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        heap = []   #to store frequency and character
        counter, ans = 0, 0
        
        for key, value in freq_map.items():
            heap.append(value)
            
        heap.sort(reverse=True)
            
        for freq in heap:
            ans += (freq)*((counter//8)+1)
            counter += 1
            
        return ans
            
        
        
        
        