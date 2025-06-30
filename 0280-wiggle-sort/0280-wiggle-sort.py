class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i&1 == 1:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]

        # TC: O(n)
        # SC: O(1)
        # Approach: lets take [3,5,2,1,6,4], odd index will have higher values and even index will have lower value. Now check for every index if this condition is not satisfied, swap with previous element.
        # 1 < 2 out of place, if we swap it will not impact as 1 < 2 and 2 < 5, so swapping them will not impact 5
        # similarly 6 > 2, swap needed, but since 6>2 and 6>1, so no impact on 1, hence we can swap
        