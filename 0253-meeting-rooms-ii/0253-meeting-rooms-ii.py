class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        j = 0
        ans = cnt = 0

        for i in range(len(start)):
            while end[j] <= start[i]:
                cnt -= 1
                j += 1

            cnt += 1
            ans = max(cnt, ans)

        return ans

