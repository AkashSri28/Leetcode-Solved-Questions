class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7
        # mem = dict()

        # def solve(n, num):
        #     if n < 0 or num**x > n:
        #         return 0
        #     if n == num**x:
        #         return 1

        #     if (n, num) not in mem:
        #         a = solve(n - num**x, num+1)
        #         b = solve(n, num+1)
        #         mem[(n, num)] = (a+b)%mod
        #     return mem[(n, num)]

        # return solve(n, 1)

        powers = []
        i = 1
        while True:
            p = pow(i, x)
            if p > n:
                break
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]
        