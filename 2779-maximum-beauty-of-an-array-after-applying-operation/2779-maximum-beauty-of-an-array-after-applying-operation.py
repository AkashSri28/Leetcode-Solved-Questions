class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ls = []
        ans = float('-inf')
        
        for n in nums:
            ls.append((n-k, -1))
            ls.append((n+k, 1))
            
        ls.sort()
        
        cnt = 0
        for num, f in ls:
            if f == -1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt -= 1
                
        return ans
    
    # TC: O(2n)
    #     SC: O(n)
    #         Approach: we need to find a point where maximum intervals overlap
        