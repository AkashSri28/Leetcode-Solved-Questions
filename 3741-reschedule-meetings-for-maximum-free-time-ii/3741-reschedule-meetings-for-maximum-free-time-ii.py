class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        gaps.append(startTime[0] - 0)
        n = len(startTime)

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])

        gaps.append(eventTime - endTime[n-1])
        ans = max(gaps)
        l_max = 0
        r_max = [0]*(n+1)

        for i in range(n-1, -1, -1):
            r_max[i] = max(r_max[i+1], gaps[i+1])

        for i in range(n):
            d = endTime[i] - startTime[i]
            if d <= max(l_max, r_max[i+1]):
                ans = max(ans, gaps[i]+gaps[i+1]+d)
            # if d <= max(gaps[i], gaps[i+1]):
            ans = max(ans, gaps[i]+gaps[i+1])
            l_max = max(l_max, gaps[i])

        return ans

        