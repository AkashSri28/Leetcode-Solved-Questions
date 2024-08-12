class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = [], k
        temp = self.heap
        
        for n in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            else:
                top = heapq.heappop(self.heap)
                element = max(n, top)
                heapq.heappush(self.heap, element)        

                
    def add(self, val: int) -> int:
        temp = self.heap
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            top = heapq.heappop(self.heap)
            element = max(val, top)
            heapq.heappush(self.heap, element)  

        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)