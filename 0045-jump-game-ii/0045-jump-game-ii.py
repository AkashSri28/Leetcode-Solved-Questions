class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        cnt = 0

        while i < n-1:
            if i+nums[i] >= n-1:
                return cnt+1
            max_i = 0
            nex = i
            j = i+1
            while j < i+nums[i]+1:
                if max_i < j+ nums[j]:
                    max_i = j + nums[j]
                    nex = j
                j += 1
            i = nex
            cnt += 1

        return cnt

        # TC: O(n)
        # SC: O(1)
        # Approach: For every index see farthest it can reach, if it can cross n-1, return cnt+1. Otherwise, find from possible choices index j which can help in moving max distance

        