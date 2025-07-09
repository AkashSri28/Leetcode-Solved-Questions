class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        ls = []
        ls.append(startTime[0] - 0)

        for i in range(1, n):
            ls.append(startTime[i] - endTime[i-1])

        ls.append(eventTime - endTime[n-1])

        s, i = 0, 0
        while i < k+1:
            s += ls[i]
            i += 1
        
        ans = s
        j = i
        i = 0
        while j < len(ls):
            s += ls[j]
            s -= ls[i]
            ans = max(ans, s)
            i += 1
            j += 1

        return ans




        

        