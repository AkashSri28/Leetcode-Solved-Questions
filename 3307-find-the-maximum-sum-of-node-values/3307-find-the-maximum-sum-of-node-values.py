class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = sum(nums)
        n = len(nums)
        delta = [0]*n

        for i in range(n):
            delta[i] = (nums[i]^k) - nums[i]

        delta.sort(reverse=True)

        i = 0
        while i < n and i+1 < n:
            s = delta[i]+ delta[i+1]
            if s <= 0:
                break
            res += s
            i += 2

        return res

        # TC: O(nlogn)
        # SC: O(n)
        # Approach:if we change a node 2 times, it will return to its original value. Hence we will try update only a value once but in pairs. Update all values and check what values will contribute in updating res
        