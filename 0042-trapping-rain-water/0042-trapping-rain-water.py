class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rmax = [0]*n
        ans = 0

        for i in range(n-2, 0, -1):
            rmax[i] = max(height[i+1], rmax[i+1])

        lmax = height[0]
        for i in range(1, n-1):
            h = min(lmax, rmax[i])
            if h > height[i]:
                ans += h - height[i]
            lmax = max(lmax, height[i])

        return ans


        