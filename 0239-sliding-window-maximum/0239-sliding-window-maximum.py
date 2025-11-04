class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        ans = []
        for i in range(n):
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if i < k-1:
                continue

            while len(q) > 0 and q[0] <= i-k:
                q.popleft()

            ans.append(nums[q[0]])
        return ans


        