class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        stack.append((0, -1))
        
        for index, height in enumerate(heights):
            start = index
            while stack[-1][0] > height:
                curr_height, i2 = stack.pop()
                curr_area = curr_height*(index-i2)
                area = max(area, curr_area)
                start = i2
                
            stack.append((height, start))
            
        while stack:
            curr_height, i2 = stack.pop()
            curr_area = curr_height*(len(heights)-i2)
            area = max(area, curr_area)
            
        return area
        
# TC: O(n)
#     SC: O(n)    #stack
#         Approach: Every height can be stretched to right unless there is something smaller. And to left it can be stretched until elements taller to it are present