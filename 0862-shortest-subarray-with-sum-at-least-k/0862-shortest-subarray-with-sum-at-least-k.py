class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        q = deque()
        ans = float('inf')

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(n+1):
            while q and prefix[i] - prefix[q[0]] >= k:
                ans = min(ans, i-q.popleft())

            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)

        return ans if ans != float('inf') else -1
        