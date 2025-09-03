class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def compare(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            return b[1] - a[1]
        points.sort(key=cmp_to_key(compare))
        n = len(points)
        ans = 0
        for i in range(n):
            topY = points[i][1]
            limitY = float('-inf')
            for j in range(i + 1, n):
                bottomY = points[j][1]
                if bottomY <= topY and bottomY > limitY:
                    ans += 1
                    limitY = bottomY
                    if bottomY == topY:
                        break
                
        return ans

        # TC: O(nlogn + n**2)
        # SC: O(1)
        # Approach: Sort to check points from left. Keep track of tallest point in between. If the tallest point is less than bottomY, then count this pair
        

        