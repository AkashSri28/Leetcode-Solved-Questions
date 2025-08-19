class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != 0:
                i += 1
                continue
            j = i
            while j < n and nums[j] == 0:
                j += 1
            l = j - i
            # print("l ", l)
            ans += (l*(l+1))//2
            i = j

        return ans

        