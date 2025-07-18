class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        left = [0]*(n*2)
        min_heap = []

        s = 0
        for i in range(2*n):
            s += nums[i]
            heapq.heappush(min_heap, -nums[i])
            if len(min_heap) > n:
                num = heapq.heappop(min_heap)
                s -= -num
            left[i] = s

        max_heap = []
        s = 0
        right = [0]*(3*n)
        for i in range(3*n-1, n-1, -1):
            s += nums[i]
            heapq.heappush(max_heap, nums[i])
            if len(max_heap) > n:
                num = heapq.heappop(max_heap)
                s -= num
            right[i] = s
        
        ans = float('inf')
        for i in range(n-1, 2*n):
            ans = min(ans, left[i]-right[i+1])

        return ans

        # TC: O(3*n)
        # SC: O(3*n)
        # Approach: In worst case we can include will 2n index in left array. So till 2nd check min possible value at each index. Similarly do it from right. Now find this difference at index i