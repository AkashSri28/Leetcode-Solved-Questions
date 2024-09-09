class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n, cnt, major = len(nums), 1, nums[0]
        for i in range(1, n):
            if nums[i] == major:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    major = nums[i]
                    cnt = 1
        
        return major
        
        