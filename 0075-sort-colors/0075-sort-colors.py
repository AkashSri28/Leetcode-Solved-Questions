class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
        
# Clarification: will clarify if only 3 values exist in nums, size of nums
# Brute Force: sort O(nlogn)
# Approach: will use 3 pointers i, j, k, i will point where next 0 will come, k will point where next 2 will come, if we see a 1 will move forward as i will get stuck here
# TC: O(n)
# SC: O(1)
# Testing: check when data is sorted, reverse sorted, only 1 value type is there
        