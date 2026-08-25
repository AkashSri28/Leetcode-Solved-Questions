class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        n = len(bloomDay)
        if (n < m*k):
            return -1

        ans = -1

        while low <= high:
            mid = (low + high)//2
            curr = 0
            group = 0
            for i in range(n):
                if mid >= bloomDay[i]:
                    curr += 1
                else:
                    curr = 0
                if curr == k:
                    group += 1
                    curr = 0
            if group >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


            
        