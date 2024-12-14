class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        max_deque = deque()
        min_deque = deque()
        l = 0
        count = 0

        for r in range(n):
            # Maintain the max_deque (decreasing order)
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            max_deque.append(r)

            # Maintain the min_deque (increasing order)
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            min_deque.append(r)

            # Shrink the window if condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                l += 1
                # Remove indices outside the window
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()

            # Add all valid subarrays ending at r
            count += (r - l + 1)

        return count
            
            
        