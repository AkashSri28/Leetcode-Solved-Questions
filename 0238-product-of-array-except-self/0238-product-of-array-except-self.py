class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod, right_prod = [1]*(n+1), [1]*(n+1)

        for i in range(n-1, -1, -1):
            right_prod[i] = nums[i]*right_prod[i+1]

        ans = [0]*n
        for i in range(n):
            left_prod[i+1] = nums[i]*left_prod[i]
            ans[i] = left_prod[i]*right_prod[i+1]

        return ans

# TC: O(2n)
# SC: O(1)
# Clarification: 
# Brute Force:
# Approach: 
# Testing:

        