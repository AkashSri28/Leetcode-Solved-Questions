class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] - nums[i] <= k:
                j += 1
            ans += 1
            i = j
        
        return ans

        # TC: O(nlogn)
        # SC: O(n)    # Tim sort uses O(n) space
        # Approach: Sort and find subarray which satisfy the condition
        