class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        seen = set()
        score = 0
        
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num, index))
            
        while heap:
            num, index = heapq.heappop(heap)
            if index not in seen:
                seen.add(index)
                seen.add(index-1)
                seen.add(index+1)
                score += num
                
        return score
    
    # TC: O(nlogn) #heap
    #     SC: O(n)    #heap
    #         Approach: Use heap to find min element and for each min element mark it and its neighbours in seen
            
        