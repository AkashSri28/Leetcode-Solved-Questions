class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_seen = 0
        max_sum = 0
        ls = []
        for s, e, v in events:
            ls.append((s, True, v))
            ls.append((e+1, False, v))
            
        for t, f, v in sorted(ls):
            if f:
                max_sum = max(max_sum, max_seen+v)
            else:
                max_seen = max(max_seen, v)
                
        return max_sum
        
        