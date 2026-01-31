class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j+1

        # TC: O(n)
        # SC: O(1)
        # Approach: keep a pointer j to track all unique elements, use i to iterate over elements, everytime a new element is seen, move j and place new element there
        