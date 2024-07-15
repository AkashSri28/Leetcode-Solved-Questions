class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, length = 0, len(nums)
        j = length
        
        while i<j:
            if nums[i] == val:
                j -= 1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
            else:
                i += 1
        return j

# TC: O(n)
# SC: O(1)
# Approach: Variation of DNF algorithm, keep j to track val values seen so far