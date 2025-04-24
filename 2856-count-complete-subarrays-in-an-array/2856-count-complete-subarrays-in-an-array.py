class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = ans = j = 0
        n = len(nums)
        mem = dict()
        freq = Counter(nums)
        target = len(freq)

        for i in range(n):
            if nums[i] not in mem:
                cnt += 1
                mem[nums[i]] = 0
            mem[nums[i]] += 1

            while cnt >= target:
                ans += (n-i)
                mem[nums[j]] -= 1
                if mem[nums[j]] == 0:
                    cnt -= 1
                    del mem[nums[j]]
                j += 1

        return ans 

        