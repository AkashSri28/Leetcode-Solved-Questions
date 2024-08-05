class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res, counter = "", 0
        map = defaultdict(int)      #O(n)
        
        for a in arr:       #O(n)
            map[a] += 1
            
        for key, value in map.items():  #O(n)
            if value > 1:
                continue
            counter += 1
            if counter == k:
                res = key
                break        
        
        return res
        
        # TC: O(n)
        #     SC: O(n)
        #         Approach: we need to store all strings as duplicate can come later as well
        #             now check frequencies and count where frequency is 1