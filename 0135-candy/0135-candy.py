class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        # ans = [1]*N
        # heap = []

        # for i, r in enumerate(ratings):
        #     heapq.heappush(heap, (r, i))

        # while heap:
        #     r, i = heapq.heappop(heap)
        #     if i-1 >= 0 and ratings[i-1] < ratings[i] and ans[i] <= ans[i-1]:
        #         ans[i] = 1+ans[i-1]
        #     if i+1 < N and ratings[i+1] < ratings[i] and ans[i] <= ans[i+1]:
        #         ans[i] = 1+ans[i+1]

        # return sum(ans)

        # TC: O(nlogn)
        # SC: O(n)
        # Approach: always pick lowest value and update it according to its neighbours

        left = [1]*N
        right = [1]*N
        res = 0

        for i in range(1, N):
            if ratings[i-1] < ratings[i]:
                left[i] = 1+left[i-1]

        for i in range(N-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                right[i] = 1+right[i+1]

        for a, b in zip(left, right):
            res += max(a, b)

        return res

        # TC: O(n)
        # SC: O(n)
        # Approach: first satisfy for left side elements then satisfy for right side elements





        