class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        dp = [1]*n
        
        for i in range(1, n):
            if nums[i]&1 != nums[i-1]&1:
                dp[i] = 1+dp[i-1]
              
        ans = []
        for s, e in queries:
            if dp[e] >= (e-s)+1:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: For each index find length of longest alternate string ending, now check if length of string is greater than given range
        