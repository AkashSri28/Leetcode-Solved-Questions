class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0
        while len(nums) >= 2 and nums[0] < k:
            cnt += 1
            num1, num2 = heapq.heappop(nums), heapq.heappop(nums)
            op = 2*min(num1, num2) + max(num1, num2)
            heapq.heappush(nums, op)

        return cnt

        