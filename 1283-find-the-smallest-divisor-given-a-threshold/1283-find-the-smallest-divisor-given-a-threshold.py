class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = 0

        while low <= high:
            mid = (low + high)//2
            s = 0
            s = sum((num + mid - 1) // mid for num in nums)
            if s <= threshold:
                ans = mid
                high = mid-1
            else: 
                low = mid + 1

        return ans

# Clarification: range of values in nums
# Brute Force: take all values from 1 to max(nums), O(n)
# Approach: using BS over answer space
# TC: O(max(num)*logn)
# SC: O(1)
# Testing: nums is sorted, not sorted, nums elements are prime
# Time: 7 mins
        