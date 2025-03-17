class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val in freq.values():
            if val%2 == 1:
                return False

        return True

        # TC: O(n)
        # SC: O(n)
        # Approach: to find a pair, even occurances should be present in nums
