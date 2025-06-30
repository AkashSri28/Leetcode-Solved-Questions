class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        mod = 10**9+7

        # Precompute all powers of 2 up to n
        power = [1] * (n)
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod

        nums.sort()
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
            ans = (ans + power[j - i]) % mod

        return ans

        # TC: O(nlogn)
        # SC: O(n)
        # Approach: For each number check which last element can form a solution with this. For this we can use binary search to find last element. Now number of combinations = 2**(j-i), 1st number will stay in combination, others may or may not be there [3, .....]. Calculating power of 2 early help in improving complexity
        