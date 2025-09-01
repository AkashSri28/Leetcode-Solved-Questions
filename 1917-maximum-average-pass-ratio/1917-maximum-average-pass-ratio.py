class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        def gain(p, t):
            return (p+1)/(t+1) - p/t

        for c in classes:
            p, t = c
            r = gain(p, t)
            heapq.heappush(heap, (-r, (p, t)))

        while extraStudents:
            r, (p, t) = heapq.heappop(heap)
            r1 = gain(p+1, t+1)
            heapq.heappush(heap, (-r1, (p+1, t+1)))
            extraStudents -= 1
            # print(heap)

        n = len(classes)
        s = 0
        for i in range(n):
            r, (p, t) = heap[i]
            s += p/t

        return s/n

        # TC: O(n+e*logn+n)
        # SC: O(n)
        # Approach: we need to update classes where difference after addition will be maximum. So we need to get values by gain. We need to maximum overall pass ratio and not individual pass ratios 






        
        