class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mem = dict()
        j = 0
        s = 0
        ans = s

        for i in range(n):
            while nums[i] in mem:
                s -= nums[j]
                mem[nums[j]] -= 1
                if mem[nums[j]] == 0:
                    del mem[nums[j]]
                j += 1
            
            s += nums[i]
            mem[nums[i]] = 1
            ans = max(ans, s)

        return ans

        