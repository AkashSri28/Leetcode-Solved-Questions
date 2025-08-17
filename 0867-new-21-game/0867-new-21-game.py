class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = dict()
        window_sum = 0
        for i in range(k, k+maxPts):
            if i <= n:
                dp[i] = 1
                window_sum += 1
            else:
                dp[i] = 0

        for i in range(k-1, -1, -1):
            dp[i] = window_sum/maxPts
            window_sum = window_sum + dp[i] - dp[i+maxPts]

        return dp[0]

        # TC: O(k+maxPts)
        # SC: O(k+maxPts)
        # Approach: We need to find probability of reaching a node starting from 0. If the leaf node is between k and n, we return 1, if above n, we return 0. If below k we find again. Lets reverse the solution, we start writing probability from back. So for all nodes between k and n, probability will be 1, above n till maxPts it will be 0. Now for k-1 and below, maintain a running sum and calculate probability
        