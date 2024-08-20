class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slow, fast, ans = 1, max(piles), sum(piles)
        while slow <= fast:
            mid = (slow + fast)//2
            k = 0
            for p in piles:
                k += math.ceil(p/mid)
                
            if k <= h:
                ans = min(ans, mid)
                fast = mid - 1
            else:
                slow = mid + 1            
            
        return ans
        