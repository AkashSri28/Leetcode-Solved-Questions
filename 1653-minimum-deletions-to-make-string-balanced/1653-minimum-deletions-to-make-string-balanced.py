class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a_right, count_b_left, res = s.count('a'), 0, float('inf')
        
        for ch in s:
            if ch == 'a':
                count_a_right -= 1
            
            res = min(res, count_a_right + count_b_left)
            
            if ch == 'b':
                count_b_left += 1
        
        return res
        
        