class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        seen = set()
        for num in nums:
            if num not in seen and num > 0:
                res += num
                seen.add(num)

        if res == 0:
            res = max(nums)
        return res

        # TC: O(n)
        # SC: O(1)
        # Approach: We need to add only positive integers to increase sum. All since each element can be added only once, maintain a set. For edge case when all elements are negative, return max(nums)
        