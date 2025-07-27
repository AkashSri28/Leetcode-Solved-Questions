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

        # TC: O(n)
        # SC: O(1)
        # Approach: We need to cnt values only once if consecutive values are equal. Will move from left to right and store prev non equal value, now for current will move to rightmost index if values are equal. This way i+1 will give next non equal value.