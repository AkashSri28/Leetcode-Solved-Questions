class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        stack = []
        for meeting in meetings:
            s, e = meeting
            while stack and stack[-1][1] >= s:
                last = stack.pop()
                s, e = min(last[0], s), max(last[1], e)
            stack.append([s, e])

        cnt = 0
        while stack:
            s, e = stack.pop()
            cnt += (e - s + 1)

        return days - cnt
            
        