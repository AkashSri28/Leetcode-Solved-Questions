class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def find_slope(point_1, point_2):
            x1, y1 = point_1
            x2, y2 = point_2
            dy = y2-y1
            if dy == 0:
                return 0
            dx = x2 - x1
            if dx == 0:
                return float(inf)
            return dy/dx
        
        n = len(points)
        if n == 1:
            return 1
        ans = 0
        for i in range(n-1):
            slope_dict = defaultdict(int)
            for j in range(i+1, n):
                slope = find_slope(points[i], points[j])
                slope_dict[slope] += 1
            
            ans = max(ans, 1+max(slope_dict.values()))
            
        return ans
        