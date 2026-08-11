class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


        

# TC: O(n)
# SC: O(1)
# Clarification: will clarify range, nums size
# Brute Force:
# Approach: 
# Testing: