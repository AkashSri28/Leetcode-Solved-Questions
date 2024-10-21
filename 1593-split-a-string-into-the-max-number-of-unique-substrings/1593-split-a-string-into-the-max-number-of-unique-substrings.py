class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        
        def helper(index, seen):
            if index == n:
                return len(seen)
            
            max_splits = 0
            for i in range(index, n):
                s1 = s[index: i+1]
                if s1 not in seen:
                    seen.add(s1)
                    max_splits = max(max_splits, helper(i+1, seen))
                    seen.remove(s1)
                    
            return max_splits
        
        seen = set()
        return helper(0, seen)
        