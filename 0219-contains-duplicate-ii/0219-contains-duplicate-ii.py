class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mem = {}
        for idx, n in enumerate(nums):
            if n in mem and idx - mem[n] <= k:
                return True
            mem[n] = idx                

        return False

        # TC: O(n)
        # SC: O(n)
        # Approach: check from left and store index if new element is seen, or condition didnt satisfy.

        