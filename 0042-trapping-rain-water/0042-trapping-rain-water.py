class Solution:
    def trap(self, height: List[int]) -> int:
        max_height_left = [0]*len(height)
        max_height_right = [0]*len(height)
        res = 0
        
        max_height = height[0]
        for i in range(1, len(height)):
            max_height_left[i] = max_height
            max_height = max(max_height, height[i])
            
        max_height = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_height_right[i] = max_height
            max_height = max(max_height, height[i])
            
        for i in range(len(height)):
            water_height = min(max_height_left[i], max_height_right[i])
            if height[i] < water_height:
                res += water_height - height[i]
                
        return res
    
# TC: O(n)
#     SC: O(n) #for storing left max height and right max height
#         Approach: for every index we need to left and right max possible height
#             now if min of left and right max height is greater than current height
#             that means water can be stored
            
                
        