class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low, high, ans = 0, x//2, 0
        while low <= high:
            mid = (low+high)//2
            if mid*mid > x:
                high = mid - 1
            else:
                ans = mid
                low = mid+1
        return ans
        