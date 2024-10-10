class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = -1
        len_nums = len(nums)
        max_right = [0]*len_nums
        maxi = -1
        for i in range(len_nums-1, -1, -1):
            maxi = max(nums[i], maxi)
            max_right[i] = maxi
            
        j = 0
        for i in range(len_nums):
            while j < len_nums and max_right[j] >= nums[i]:
                if nums[i] <= nums[j]:
                    ans = max(ans, j-i)
                j += 1
                
                    
        return ans
                
                
        