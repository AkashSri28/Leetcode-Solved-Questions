class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        flag = True
        ans = []
        nums.sort()
        n = len(nums)

        i = 0
        while i < n:
            if nums[i+2] - nums[i] > k:
                flag = False
                break
            i = i+3

        if flag:
            i = 0
            while i < n:
                row = nums[i:i+3]
                ans.append(row)
                i += 3
        
        return ans

        