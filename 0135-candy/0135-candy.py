class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        ans = [1]*N
        heap = []

        for i, r in enumerate(ratings):
            heapq.heappush(heap, (r, i))

        while heap:
            r, i = heapq.heappop(heap)
            if i-1 >= 0 and ratings[i-1] < ratings[i] and ans[i] <= ans[i-1]:
                ans[i] = 1+ans[i-1]
            if i+1 < N and ratings[i+1] < ratings[i] and ans[i] <= ans[i+1]:
                ans[i] = 1+ans[i+1]

        return sum(ans)




        