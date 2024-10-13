class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []   #(num, k, idx)
        max_val = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
            
        ans_range = [float('-inf'), float('inf')]
        
        while heap:
            num, k, idx = heapq.heappop(heap)
            
            if max_val - num < ans_range[1] - ans_range[0]:
                ans_range = [num, max_val]
                
            idx += 1
            
            if idx == len(nums[k]):
                break
            else:
                max_val = max(max_val, nums[k][idx])
                heapq.heappush(heap, (nums[k][idx], k, idx))
        
        return ans_range
    
    # TC: O(n*logk)
    #     SC: O(k)
    #         Approach: We need to find a set which includes elements from all lists and difference is minimum. We can try removing min element from list and check range. Similar to merge k sorted lists
            
            
        