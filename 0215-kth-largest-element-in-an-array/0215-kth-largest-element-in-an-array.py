class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        n = len(nums)

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


        