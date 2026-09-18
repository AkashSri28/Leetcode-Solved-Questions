class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        low, high = 1, n-2
        while low <= high:
            mid = (low + high)//2
            if mid % 2 == 0:
                if nums[mid+1] == nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[mid-1] == nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
        return nums[low]
        