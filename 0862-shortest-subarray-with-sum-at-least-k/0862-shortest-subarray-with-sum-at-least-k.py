class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = deque()
        q.append((0, 0))
        ans = float('inf')
        curr_sum = 0

        for idx, n in enumerate(nums):
            curr_sum += n

            if curr_sum >= k:
                ans = min(ans, idx+1)

            while q and q[-1][0] > curr_sum:
                # print(curr_sum)
                q.pop()

            q.append((curr_sum, idx+1))

            while q and curr_sum - q[0][0] >= k:
                num, left_idx = q.popleft() 
                ans = min(ans, idx+1 - left_idx)

        return ans if ans != float('inf') else -1
        