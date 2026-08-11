class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = 0
        mem = defaultdict(int)
        mem[0] = 1
        ans = 0
        for num in nums:
            curr += num
            if curr - k in mem:
                ans += mem[curr - k]

            mem[curr] += 1

        return ans



        