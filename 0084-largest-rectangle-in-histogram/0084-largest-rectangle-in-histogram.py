class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = [-1]*n, [-1]*n
        stack = []

        for i in range(n):
            while stack and height[stack[-1]] >= height[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n-1, -1, -1):
            while stack and height[stack[-1]] >= height[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            w = right[i] - left[i] - 1
            ans = max(ans, w*height[i])

        return ans

        