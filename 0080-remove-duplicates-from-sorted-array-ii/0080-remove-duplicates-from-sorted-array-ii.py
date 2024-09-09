class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        i, j = -1, 0
        while j < len(nums):
            if freq_map[nums[j]] != 2:
                freq_map[nums[j]] += 1
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
        return i+1