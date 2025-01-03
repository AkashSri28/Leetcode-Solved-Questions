class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        ans = 0

        for i in range(len(nums)-1):
            curr += nums[i]
            total -= nums[i]
            if curr >= total:
                ans += 1

        return ans
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: Use a pointer to split sum. Calculate current sum and update total sum according to pointer

        