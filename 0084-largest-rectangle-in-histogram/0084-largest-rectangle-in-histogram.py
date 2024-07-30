class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [], float('-inf')
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                start = idx
                area = h*(index - start)
                max_area = max(area, max_area)                
                
            stack.append([start, height])
        
        while stack:
            idx, h = stack.pop()
            start = idx
            area = h*(len(heights) - start)
            max_area = max(area, max_area)  
        
        return max_area
        
# TC: O(n)
#     SC: O(n)    #stack
#         Approach: Every height can be stretched to right unless there is something smaller. And to left it can be stretched until elements taller to it are present