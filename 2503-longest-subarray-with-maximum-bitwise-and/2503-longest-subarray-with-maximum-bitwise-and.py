class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == max_and:
                j += 1
            ans = max(ans, j-i)
            i = j+1

        return ans  
        