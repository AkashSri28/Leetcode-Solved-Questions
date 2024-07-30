class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        col = len(matrix[0])
        curr = [0]*col
        max_area = float('-inf')
        
        def find_max_area_row(curr):
            stack, max_area_in_row = [], float('-inf')
            
            for index, height in enumerate(curr):
                start = index
                while stack and stack[-1][1] > height:
                    i, h = stack.pop()
                    area = h*(index-i)
                    max_area_in_row = max(max_area_in_row, area)
                    start = i
                    
                stack.append([start, height])
            
            while stack:
                i, h = stack.pop()
                area = h*(len(curr)-i)
                max_area_in_row = max(max_area_in_row, area)
                
            return max_area_in_row
        
        for row in matrix:
            for i in range(col):
                if row[i] == "0":
                    curr[i] = 0
                    continue
                curr[i] = curr[i]+int(row[i])
            max_area = max(max_area, find_max_area_row(curr))
            
        return max_area
        