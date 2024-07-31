class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)  # dp[i] will hold the minimum height for the first i books

        for i in range(1, n + 1):
            width = 0
            max_height = 0
            dp[i] = float('inf')

            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)

        return dp[n]
        