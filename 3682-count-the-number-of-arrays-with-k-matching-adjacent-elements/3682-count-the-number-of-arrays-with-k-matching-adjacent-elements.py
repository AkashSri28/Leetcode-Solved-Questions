class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # n-1Ck*m*(m-1)^(n-k-1)
        # ((n-1)!/(n-1-k)!*k!)*m*(m-1)^(n-k-1)
        MOD = 1000000007
        factorial = [0]*n
        factorial[0] = 1

        for i in range(1, n):
            factorial[i] = (i*factorial[i-1])%MOD

        def power(a, b):
            res = 1
            while b > 0:
                if b&1 == 1:
                    res = (res*a)%MOD
                b = b>>1
                a = (a*a)%MOD
            return res
        
        # Fermat's Little Theorem to compute nCr % MOD
        def nCr(n, r):
            if r > n:
                return 0
            num = factorial[n]
            denom = (power(factorial[r], MOD - 2) * power(factorial[n - r], MOD - 2)) % MOD
            return (num * denom) % MOD

        # Final result using the formula
        result = nCr(n - 1, k)
        result = (result * m) % MOD
        result = (result * power(m - 1, n - k - 1)) % MOD

        return result