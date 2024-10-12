class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for l, r in intervals:
            heapq.heappush(heap, [l, 0])
            heapq.heappush(heap, [r, 1])
            
        ans, cnt = 0, 0
        
        while heap:
            i, flag = heapq.heappop(heap)
            if flag:
                cnt -= 1
            else:
                cnt += 1
            ans = max(ans, cnt)
            
        return ans
            
        