class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        mod = 10**9+7
        for i in range(n):
            if nums[i]*2 > target:
                break
            l, r = i, n-1
            j = i
            while l <= r:
                m = (l+r)//2
                if nums[m] + nums[i] <= target:
                    j = m
                    l = m+1
                else:
                    r = m-1
            ans = (ans%mod + pow(2, j-i)%mod)%mod

        return ans
        