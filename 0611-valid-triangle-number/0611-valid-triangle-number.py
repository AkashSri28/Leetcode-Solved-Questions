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

        # TC: O(n^2)
        # SC: O(1)
        # Approach: 3 points can form a triangle if and only if a+b > c. So we sort nums and check for all pairs a, b where a+b > c

        