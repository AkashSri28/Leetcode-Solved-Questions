class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n

        for i, num in enumerate(nums):
            ans[i] = nums[num]

        return ans
        
        # TC: O(n)
        # SC: O(1)
        # Approach: using enumerate we can find where to number and what number to place