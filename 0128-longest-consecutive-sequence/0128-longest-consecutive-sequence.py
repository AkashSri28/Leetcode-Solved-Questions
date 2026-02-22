class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        ans = cnt = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                cnt += 1
                ans = max(ans, cnt)
            elif nums[i] == nums[i-1]:
                continue
            else:
                cnt = 1

        return ans


        