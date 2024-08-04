class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        res = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                heapq.heappush(heap, sum)
                
        for i in range(1, left):
            heapq.heappop(heap)
            
        for i in range(right-left+1):
            res += heapq.heappop(heap)
            
        return res%(1000000007)
        
        
        
        
        
        
        
        
        
        
        
        # Approach: since we need first R-L elements we can use heap, rather than sorting whole result