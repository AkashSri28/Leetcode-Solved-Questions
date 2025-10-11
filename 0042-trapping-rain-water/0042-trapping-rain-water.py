class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, lmax, rmax = 0, len(height)-1, 0, 0
        ans = 0
        while l < r:
            if height[l] <= height[r]:
                if lmax > height[l]:
                    ans += lmax - height[l]
                elif lmax < height[l]:
                    lmax = height[l]
                l += 1
            else:
                if rmax > height[r]:
                    ans += rmax - height[r]
                elif rmax < height[r]:
                    rmax = height[r]
                r -= 1
        return ans
