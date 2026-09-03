class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m*n
        ans = 1
        while low <= high:
            mid = (low + high)//2
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid//i, n)
            if cnt >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        