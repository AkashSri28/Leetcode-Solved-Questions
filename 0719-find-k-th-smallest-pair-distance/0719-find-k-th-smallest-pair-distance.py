class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check_count(nums, mid, n):
            i = 0
            cnt = 0
            for j in range(n):
                while nums[j] - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        n = len(nums)
        low, high = 0, nums[n-1] - nums[0]
        ans = -1
        
        while low <= high:
            mid = (low + high)//2
            cnt = check_count(nums, mid, n)

            if cnt >= k:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans
