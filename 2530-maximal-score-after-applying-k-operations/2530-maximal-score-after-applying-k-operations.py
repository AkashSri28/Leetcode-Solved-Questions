class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []   #(num, idx)
        
        for i, n in enumerate(nums):
            heapq.heappush(max_heap, (-1*n, i))
            
        score = 0
        while k > 0:
            k -= 1
            num, idx = heapq.heappop(max_heap)
            num = -1*num
            score += num
            num = math.ceil(num/3)
            heapq.heappush(max_heap, (-1*num, idx))
            
        return score
            
        