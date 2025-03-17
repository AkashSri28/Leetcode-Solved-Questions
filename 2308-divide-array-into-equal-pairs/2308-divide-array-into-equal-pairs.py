class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val in freq.values():
            if val%2 == 1:
                return False

        return True
