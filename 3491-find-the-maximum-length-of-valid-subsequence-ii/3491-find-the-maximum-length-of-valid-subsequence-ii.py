class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0]*n for _ in range(k)]
        res = 0

        for i in range(n-2, -1, -1):
            num = nums[i]
            for j in range(i+1, n):
                m = (num + nums[j])%k
                if dp[m][i] < dp[m][j]+1:
                    dp[m][i] = dp[m][j]+1
                    res = max(res, dp[m][i])
        
        return res+1

        # TC: O(n^2)
        # SC: O(n*k)
        # Approach: there can [0....k-1] results when dividing by k. We can group pairs resulting same value after mod together. To store that use 2D matrix to count the numbers with same value after mod

        