class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9+7
        mem = dict()

        def solve(n, num):
            if n < 0 or num**x > n:
                return 0
            if n == num**x:
                return 1

            if (n, num) not in mem:
                a = solve(n - num**x, num+1)
                b = solve(n, num+1)
                mem[(n, num)] = (a+b)%mod
            return mem[(n, num)]

        return solve(n, 1)
        