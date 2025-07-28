class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)
        for num in nums:
            max_or |= num

        def dp(index, curr):
            if index == n:
                return 1 if curr == max_or else 0
            return dp(index+1, curr) + dp(index+1, curr|nums[index])

        return dp(0,0)

        # TC: O(2**n)
        # SC: O(n)
        # Approach: max possible or will be or of all values. Now we use recursion by selecting and ignoring elements to find if we are able to reach max_or


        