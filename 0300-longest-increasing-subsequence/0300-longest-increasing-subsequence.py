class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_LIS(i):
            if i < 0:
                return 0
            if LIS_at[i] == -1:
                LIS_at[i], cnt = 1, 0
                for j in range(i-1, -1, -1):
                    if nums[j] < nums[i]:
                        cnt = 1+find_LIS(j)
                        LIS_at[i] = max(LIS_at[i], cnt)
            return LIS_at[i]
        
        n = len(nums)
        LIS_at = [-1]*n
        LIS_at[0] = 1
        
        for i in range(n):
            find_LIS(i)
        # print(LIS_at)
        return max(LIS_at)
    
    # TC: O(n^2)
    #     SC: O(n)
    #         Approach: Find length of longest subsequence ending at i. Return max of all values.
        