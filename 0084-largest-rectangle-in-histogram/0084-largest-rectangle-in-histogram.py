class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = [-1]*n, [n]*n
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
            ans = max(ans, height[i] * (right[i] - left[i] - 1))

        return ans

        # TC: O(3n)
        # SC: O(3n)
        # Approach: Find left and right side boundary, then find area for each position

        