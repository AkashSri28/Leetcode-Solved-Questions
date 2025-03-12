class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search(target):
            l = 0
            r = len(nums)-1
            res = len(nums)
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                else:
                    res = mid
                    r = mid-1
            return res

        neg = binary_search(0)
        pos = len(nums) - binary_search(1)

        
        return pos if pos > neg else neg
        