class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:        
        n = len(nums)
        dp_left = [0]*n
        dp_right = [0]*n
        length = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp_left[i] = max(dp_left[i], 1+dp_left[j])
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    dp_right[i] = max(dp_right[i], 1+dp_right[j])
        
        for i in range(1, n-1):
            if dp_left[i] > 0 and dp_right[i] > 0:
                length = max(length, 1+dp_left[i]+dp_right[i])
            
        return n-length
            
        