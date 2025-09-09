from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)  # dp[i] = number of people who learn on day i
        dp[1] = 1
        share_sum = 0  # running sum of people currently sharing
        for i in range(2, n + 1):
            # add those who start sharing today
            if i - delay >= 1:
                share_sum = (share_sum + dp[i - delay]) % MOD
            # remove those who forget today (they stop sharing)
            if i - forget >= 1:
                share_sum = (share_sum - dp[i - forget]) % MOD
            dp[i] = share_sum

        # count those who still remember on day n (learned in last forget-1 days)
        ans = 0
        for i in range(max(1, n - forget + 1), n + 1):
            ans = (ans + dp[i]) % MOD
        return ans


        