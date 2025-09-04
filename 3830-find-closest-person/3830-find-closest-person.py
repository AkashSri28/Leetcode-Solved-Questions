class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(z-y), abs(z-x)
        if d2 < d1:
            return 1
        if d1 < d2:
            return 2
        return 0

        # TC: O(1)
        # SC: O(1)
        # Approach: calculate abs distance and return min
        