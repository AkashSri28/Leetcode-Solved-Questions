class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]   #(num)
        heapq.heapify(max_heap)
        
        # for i, n in enumerate(nums):
        #     heapq.heappush(max_heap, -1*n)
            
        score = 0
        while k > 0:
            k -= 1
            num = heapq.heappop(max_heap)
            num = -1*num
            score += num
            num = math.ceil(num/3)
            heapq.heappush(max_heap, -1*num)
            
        return score
    
    # TC: O(k*logn)
    #     SC: O(n)
    #         Approach: We will always use max value to add in score. So heapify nums and extract max in each iteration
            
        