class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        map = defaultdict(list)
        min_area = float("inf")
        for p in points:
            map[p[0]].append(p[1])
            
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                x3, y3, x4, y4 = x1, y2, x2, y1
                if y3 in map[x3] and y4 in map[x4]:
                    min_area = min(min_area, abs(y2-y1)*abs(x2-x1))
                    
        if min_area == float("inf"):
            return 0
        return min_area
        
# TC: O(n^2)
#     O(n)    creating map
#     +
#     O(n^2)  for iterating over points
    
# SC: O(n)    map
    
# Approach: if we know diagonal in a rectangle, points on other diagonal can be calculated
#     Now check if these points exist