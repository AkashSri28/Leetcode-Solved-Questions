class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [-1]*n
        mem[n-1] = 0

        def dp(i):
            if i >= n:
                return float('inf')
            if mem[i] == -1:
                ans = float('inf')
                j = nums[i]
                for k in range(1, j+1):
                    ans = min(ans, 1+dp(i+k))
                mem[i] = ans

            return mem[i] 

        return dp(0)
        