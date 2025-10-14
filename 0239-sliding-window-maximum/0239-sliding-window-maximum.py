class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # q = deque()
        # n = len(nums)
        # for i in range(k):
        #     if len(q) == 0 or q[-1] <= nums[i]:
        #         q.append(nums[i])
        # ans = []

        # for i in range(n-k+1):
        #     if q:
        #         ans.append(q[-1])
        #     j = i+k
        #     if q and q[0] == nums[i]:
        #         q.popleft()
        #     if q and q[-1] <= nums[j]:
        #         q.append(nums[j])

        # return ans

        q = deque()  # stores indices of potential max elements
        ans = []

        for i, num in enumerate(nums):
            # 1️⃣ Remove indices out of current window
            while q and q[0] <= i - k:
                q.popleft()

            # 2️⃣ Maintain decreasing order in deque
            while q and nums[q[-1]] <= num:
                q.pop()

            # 3️⃣ Add current index
            q.append(i)

            # 4️⃣ The front of the deque is the max in current window
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans

        