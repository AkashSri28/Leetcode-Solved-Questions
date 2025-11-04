class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        ans = []
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if i < k-1:
                continue

            while q and q[0] <= i-k:
                q.popleft()

            ans.append(nums[q[0]])
        return ans

        # TC: O(n)
        # SC: O(k)
        # Approach: iterate array from 0 to n index. Now everytime we see a number, we remove all smaller numbers from queue as they wont be needed once we encounter a larger number. Also keep dropping elements from front whose index is less than window size i - k


        