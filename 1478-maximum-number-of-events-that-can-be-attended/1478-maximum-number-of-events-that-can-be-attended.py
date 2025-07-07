class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()

        heap = []
        ans = 0
        j = 0

        for i in range(1, max_day+1):
            while heap and heap[0] < i:
                heapq.heappop(heap)

            while j < n and events[j][0] == i:
                heapq.heappush(heap, events[j][1])
                j += 1

            if heap:
                heapq.heappop(heap)
                ans += 1

        return ans

        # TC: O(nlogn)
        # SC: O(n)
        # Approach: we need to traverse day-wise and check which events starts on that day. We will store end dates for all events starting that day. On every day. first remove all elements which have end day less than current day. Then add all events starting from that day. Now select one element which ends first and increase count
            


        