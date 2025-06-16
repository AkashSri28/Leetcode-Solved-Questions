class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff, left = -1, float('inf')
        for i in range(len(nums)):
            if nums[i] > left:
                diff = max(diff, nums[i] - left)
            left = min(left, nums[i])

        return diff
        