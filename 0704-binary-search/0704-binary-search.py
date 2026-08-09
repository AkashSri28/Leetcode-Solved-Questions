class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if(nums[mid] == target):
                ans = mid
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return ans

# TC: O(logn)
# SC: O(1)
# Clarification: clarify if numbers are sorted, if negative numbers are included
# Brute Force: check all numbers one by one O(n)
# Approach: use binary search to guess the target, if found return, if guess > target then target can be on left of mid, high = mid -1, else low = mid + 1
# Testing: test when target is not present in nums