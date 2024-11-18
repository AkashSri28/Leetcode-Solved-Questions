class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev_i, curr_i = -1, 0
        while prev_i != curr_i:
            max_step = 0
            prev_i = curr_i
            for j in range(0, nums[prev_i]+1):
                k = prev_i+j
                if k >= len(nums)-1:
                    return True
                next_step = nums[k]+k
                if next_step > max_step:
                    max_step = next_step
                    curr_i = k
                    
            
        return False
            
                    
            
                    
            
                
            
        
        