class Solution:
    def find_min_idx(self, nums):
        min_ele, min_idx = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] < min_ele:
                min_ele = nums[i]
                min_idx = i

        return min_idx

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_idx = -1
        while k > 0:
            min_idx = self.find_min_idx(nums)
            nums[min_idx] *= multiplier
            k -= 1

        return nums
        