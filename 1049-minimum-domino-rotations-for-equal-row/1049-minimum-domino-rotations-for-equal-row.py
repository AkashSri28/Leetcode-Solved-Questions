class Solution:
    def minDominoRotations(self, top: List[int], bottom: List[int]) -> int:
        def check(x):
            rotate_top = rotate_bottom = 0
            for i in range(len(top)):
                if top[i] != x and bottom[i] != x:
                    return float('inf')
                elif top[i] != x:
                    rotate_top += 1
                elif bottom[i] != x:
                    rotate_bottom += 1
            return min(rotate_top, rotate_bottom)

        res = min(check(top[0]), check(bottom[0]))
        return res if res != float('inf') else -1
