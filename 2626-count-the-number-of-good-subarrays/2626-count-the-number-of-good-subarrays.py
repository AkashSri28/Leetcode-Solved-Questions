class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = 0
        res = 0
        freq = defaultdict(int)
        n = len(nums)
        l = 0

        for r in range(n):
            R = nums[r]
            freq[R] += 1
            cnt += (freq[R]-1)

            while cnt >= k:
                res += (n-r)
                L = nums[l]
                cnt -= (freq[L]-1)
                freq[L] -= 1
                l += 1

        return res

        