class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        mem = defaultdict(int)

        for i in range(l-1, -1, -1):
            n = nums[i]
            mem[n] += 1
            if mem[n] > 1:
                res = i+3
                return res//3

        return 0

        