from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9+7
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            cnt = 0
            for j in range(i-forget+1, i-delay+1):
                if j < 0:
                    continue
                cnt = (cnt+dp[j])%mod
            dp[i] = cnt
        ans = 0
        for i in range(n-forget+1, n+1):
            ans = (ans+dp[i])%mod

        return ans

        # TC: O(n*(delay-forget))
        # SC: O(n)
        # Approach: For each day, find number of new people on that day. New people will be contributed by people between forget+1 and delay. At the nth day find all people from n-forget+1 to n



        