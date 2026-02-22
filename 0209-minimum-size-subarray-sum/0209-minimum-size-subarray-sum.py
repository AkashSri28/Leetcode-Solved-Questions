class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = s = 0
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            s += nums[i]

            while s >= target:
                l = i-j+1
                ans = min(ans, l)
                s -= nums[j]
                j += 1

        return ans if ans != float('inf') else 0




        