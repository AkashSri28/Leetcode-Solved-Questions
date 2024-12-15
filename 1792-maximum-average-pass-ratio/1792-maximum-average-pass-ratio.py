class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(pas, total):
            return (pas+1)/(total+1)-(pas/total)
        
        max_heap = []
        
        for pas, total in classes:
            heapq.heappush(max_heap, (-gain(pas, total), pas, total))
            
        for _ in range(extraStudents):
            g, pas, total = heapq.heappop(max_heap)
            pas += 1
            total += 1
            heapq.heappush(max_heap, (-gain(pas, total), pas, total))
            
        s = 0
        while max_heap:
            gain, pas, total = heapq.heappop(max_heap)
            s += pas/total
            
        return s/ len(classes)
        