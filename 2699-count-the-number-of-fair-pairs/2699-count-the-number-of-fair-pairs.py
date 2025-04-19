class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0

        def binary_search(l, r, target):
            res = n
            while l <= r:
                mid = (l+r)//2
                x = nums[mid]
                if x >= target:
                    res = mid
                    r = mid-1
                else:
                    l = mid+1
            return res


        for i in range(n-1):
            L = binary_search(i+1, n-1, lower-nums[i])
            R = binary_search(L, n-1, upper-nums[i]+1)
            cnt += (R-L)

        return cnt

        