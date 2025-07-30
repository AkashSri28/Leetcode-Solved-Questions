class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []

        def pick_max(nums, i):
            stack = []
            dis = 0
            for num in nums:
                while stack and stack[-1] < num and dis < len(nums) - i:
                    stack.pop()
                    dis += 1
                stack.append(num)
            return stack[:i]

        def merge(max1, max2):
            res = []
            max1, max2 = deque(max1), deque(max2)
            while max1 or max2:
                if list(max1) > list(max2):
                    res.append(max1.popleft())
                else:
                    res.append(max2.popleft())
            return res

        for i in range(k+1):
            j = k-i
            max1 = pick_max(nums1, i)
            max2 = pick_max(nums2, j)
            merged = merge(max1, max2)
            if len(merged) == k:
                ans = max(ans, merged)

        return ans

        # TC: O(k*(m+n)*k)
        # SC: O(m+n)
        # Approach: To create an array of k elements we need k elements combined from nums1 and nums2. We will check all possible combination of contribution from nums1 and nums2. Now if we get an array of size, we will compare and store lexicographically largest array

