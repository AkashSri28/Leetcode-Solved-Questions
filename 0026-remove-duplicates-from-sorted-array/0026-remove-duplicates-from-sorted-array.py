class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        i, j = -1, 0
        seen = set()
        while j < len(nums):
            if nums[j] not in seen:
                seen.add(nums[j])
                i += 1
                # swap(nums, i, j)
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
        return i+1
        