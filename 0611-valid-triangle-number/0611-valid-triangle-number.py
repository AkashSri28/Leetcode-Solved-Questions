class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        nums.sort()
        for k in range(2, n):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    cnt += j-i
                    j -= 1
                else:
                    i += 1
        return cnt

        