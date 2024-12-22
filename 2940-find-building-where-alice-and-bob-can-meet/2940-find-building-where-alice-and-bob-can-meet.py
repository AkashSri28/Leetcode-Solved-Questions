class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1]*len(queries)
        groups = defaultdict(list)
        
        for i, q in enumerate(queries):
            l, r = sorted(q)
            if l == r or heights[r] > heights[l]:
                ans[i] = r
            else:
                groups[r].append((max(heights[l], heights[r]), i))
            
        min_heap = []
        for i in range(len(heights)):
            while min_heap and min_heap[0][0] < heights[i]:
                h, index = heapq.heappop(min_heap)
                ans[index] = i
                
            for h, index in groups[i]:
                heapq.heappush(min_heap, (h, index))
                
        return ans
        