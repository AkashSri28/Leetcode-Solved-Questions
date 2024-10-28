class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        cnt = defaultdict(int)
        ans = float('-inf')
        
        for i in range(n-1, -1, -1):
            sq = nums[i]**2
            if sq in cnt:
                cnt[nums[i]] = cnt[sq]+1
                ans = max(ans, cnt[nums[i]])
            else:
                cnt[nums[i]] = 1
                
                
        if ans == float('-inf'):
            return -1
        return ans
    
    # TC: O(nlogn)
    #     SC: O(n)
    #         Approach: If we know the length of streak from any point and we reach that point for current element. Length of streak for current element will be 1+ streak of next starting point
        