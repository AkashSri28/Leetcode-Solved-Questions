class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff, left = -1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] > left:
                diff = max(diff, nums[i] - left)
            else:
                left = min(left, nums[i])

        return diff

        # TC: O(n)
        # SC: O(1)
        # Approach: we need to store smallest number on left and check with every number and calculate difference
        