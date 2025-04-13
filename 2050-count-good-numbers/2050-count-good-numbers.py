class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        def power(base, exp):
            s = 1
            base %= MOD

            while exp > 0:
                if exp % 2 == 1:
                    s = (s*base)%MOD
                base = (base*base)%MOD
                exp //= 2

            return s

        even = (n+1)//2
        odd = n//2

        even_cnt = power(5, even)
        odd_cnt = power(4, odd)

        return (even_cnt*odd_cnt)%MOD 

        