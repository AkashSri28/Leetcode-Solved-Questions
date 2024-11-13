class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        
        def binary_search(l, r, target):
            res = l-1
            while l <= r:
                m = (l+r)//2
                if nums[m] < target:
                    res = m
                    l = m+1
                else:
                    r = m-1
            return res
                
        for i in range(0, len(nums)):
            right = binary_search(i+1, len(nums)-1, upper-nums[i]+1)
            left = binary_search(i+1, len(nums)-1, lower-nums[i])
            result += (right-left)
            
        return result
        