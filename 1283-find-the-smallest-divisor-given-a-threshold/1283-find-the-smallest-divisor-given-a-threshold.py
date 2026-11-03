class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = 0

        while low <= high:
            mid = (low + high)//2
            s = 0
            for num in nums:
                s += math.ceil(num/mid)
            if s <= threshold:
                ans = mid
                high = mid-1
            else: 
                low = mid + 1

        return ans


        