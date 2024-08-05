class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res, counter = "", 0
        map = defaultdict(int)
        
        for a in arr:
            map[a] += 1
            
        for key, value in map.items():
            if value > 1:
                continue
            counter += 1
            if counter == k:
                res = key
                break        
        
        return res
        