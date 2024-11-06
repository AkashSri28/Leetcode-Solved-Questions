class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        curr_max, curr_min = nums[0], nums[0]
        prev_max = 0
        
        def count_bits(n):
            return bin(n).count('1')
        
        for n in nums:
            if count_bits(n) != count_bits(curr_max):
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_min, curr_max = n, n
            else:
                curr_max = max(curr_max, n)
                curr_min = min(curr_min, n)
        
        return prev_max <= curr_min
            
            
        