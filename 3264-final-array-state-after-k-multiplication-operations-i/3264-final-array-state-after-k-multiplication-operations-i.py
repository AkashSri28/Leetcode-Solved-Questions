class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        res = [0]*len(nums)
        
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num, index))
            
        for _ in range(k):
            num, index = heapq.heappop(heap)
            num = num*multiplier
            heapq.heappush(heap, (num, index))
            nums[index] = num
            
        return nums
    
    # TC: O(k*logn)
    #     SC: O(n)
    #         Approach: we need to find smallest number at each iteration, hence min heap is used
        