class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = -1, 0, len(nums)

        while j < k:
            n = nums[j]
            if n == 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            elif n == 1:
                j += 1
            else:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
