class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        p = nums[0]

        for i in range(1, n-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] > max(p, nums[i+1]) or nums[i] < min(p, nums[i+1]):
                cnt += 1
            p = nums[i]
        return cnt