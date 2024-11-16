class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cnt = 0
        res = []
        
        for i in range(1, k):
            if nums[i] == nums[i-1]+1:
                cnt += 1
        
        if cnt == k-1:
            res.append(nums[k-1])
        else:
            res.append(-1)
            
        i, j = 0, k
        while j < len(nums):
            if nums[j] == nums[j-1]+1:
                cnt += 1
            if nums[i] == nums[i+1]-1:
                cnt -= 1
            if cnt == k-1:
                res.append(nums[j])
            else:
                res.append(-1)
            j += 1
            i += 1
            
        return res
                
            
        
            
        