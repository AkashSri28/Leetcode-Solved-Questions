class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        i = 0
        while i < n:
            if nums[i+2] - nums[i] > k:
                return []
            row = nums[i:i+3]
            ans.append(row)
            i = i+3
        
        return ans

        