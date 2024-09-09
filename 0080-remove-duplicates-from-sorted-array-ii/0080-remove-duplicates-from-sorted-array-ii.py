class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = -1, 0
        while j < len(nums):
            curr = nums[j]
            curr_freq = 0
            
            while j < len(nums) and nums[j] == curr and curr_freq < 2:
                curr_freq += 1
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
            while j < len(nums) and nums[j] == curr:
                j += 1
            
        return i+1
    
    # TC: O(n)
    #     SC: O(1)
    #         Approach: Two pointer. i will track final list ending. Now count number of curr occurance, skip all occurances once count reaches 2.