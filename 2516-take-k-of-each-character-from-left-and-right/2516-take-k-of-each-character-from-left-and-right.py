class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        char_count = Counter(s)
        target_count = defaultdict(int)
        
        for ch in 'abc':
            if char_count[ch] < k:
                return -1
            char_count[ch] = char_count[ch] - k
            
        j, ans = 0, 0
        for i in range(len(s)):
            ch = s[i]
            target_count[ch] += 1
            while j <= i and target_count[ch] > char_count[ch]:
                target_count[s[j]] -= 1
                j += 1
                
            ans = max(ans, i-j+1)
            
        return len(s)-ans
            
            
        
            
        
        