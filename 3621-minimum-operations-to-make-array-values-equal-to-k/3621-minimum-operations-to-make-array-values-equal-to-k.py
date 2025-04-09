class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()

        for num in nums:
            if num < k:
                return -1
            elif num > k:
                s.add(num)

        return len(s)

        # TC: O(n)
        # SC: O(n)
        # Approach: if we see any number less than k, then we can't reach. Now we need to find number of unique numbers greater than k. These are the operations