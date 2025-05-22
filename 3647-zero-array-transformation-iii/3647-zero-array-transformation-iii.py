class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        candidates, selected = [], []
        n = len(nums)
        queries.sort()
        ans, j = 0, 0

        for i in range(n):
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(candidates, -queries[j][1])
                j += 1

            nums[i] -= len(selected)

            while nums[i] > 0 and len(candidates) > 0 and abs(candidates[0]) >= i:
                nums[i] -= 1
                x = heapq.heappop(candidates)
                heapq.heappush(selected, abs(x))
                ans += 1

            if nums[i] > 0:
                return -1

            while len(selected) > 0 and selected[0] == i:
                heapq.heappop(selected)

        return len(queries)-ans

        