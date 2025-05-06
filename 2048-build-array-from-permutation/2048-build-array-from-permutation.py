class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n

        for i, num in enumerate(nums):
            ans[i] = nums[num]

        return ans
        