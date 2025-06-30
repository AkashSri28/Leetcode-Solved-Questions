class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        mem = dict()

        def power2(i):
            if i not in mem:
                mem[i] = 2**i
            return mem[i]

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
            ans = (ans+power2(j-i))%mod

        return ans
        