class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        mem = defaultdict(int)
        res = 0

        for i in range(l-1, -1, -1):
            n = nums[i]
            mem[n] += 1
            if mem[n] > 1:
                res = i+1
                break

        return math.ceil(res/3)

        