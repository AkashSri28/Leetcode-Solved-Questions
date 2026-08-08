class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        i, j = -1, -1
        for idx, num in enumerate(nums):
            if target - num in mem:
                i = mem[target - num]
                j = idx
                break
            mem[num] = idx

        return [i, j]

        