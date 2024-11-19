class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        memo = dict()
        ans = 0
        su = 0
        for i in range(k):
            curr = nums[i]
            su += curr
            if curr not in memo:
                memo[curr] = 1
            else:
                memo[curr] += 1
                
        if len(memo) == k:
            ans += max(su, ans)
            
        i, j = 0, k
        while j < len(nums):
            memo[nums[i]] -= 1
            su -= nums[i]
            if memo[nums[i]] == 0:
                del memo[nums[i]]
                
            i += 1
            su += nums[j]
            if nums[j] not in memo:
                memo[nums[j]] = 1
            else:
                memo[nums[j]] += 1
                
            j += 1
            
            if len(memo) == k:
                ans = max(ans, su)
                
        return ans
                
        