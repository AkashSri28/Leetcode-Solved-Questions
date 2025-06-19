class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        ans = cnt = 0

        for start, end in intervals:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, 0))
        
        while heap:
            time, flag = heapq.heappop(heap)
            if flag == 1:
                cnt += 1
            else:
                cnt -= 1
            ans = max(ans, cnt)

        return ans