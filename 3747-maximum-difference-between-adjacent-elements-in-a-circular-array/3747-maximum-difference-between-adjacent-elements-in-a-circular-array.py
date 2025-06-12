class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            j = (i+1)%n
            diff = abs(nums[i]-nums[j])
            ans = max(ans, diff)

        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: keep calculating current number and next number difference

        