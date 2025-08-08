class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        
        mem = dict()

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            if (a,b) not in mem:
                mem[(a,b)] = 0.25*(dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50) + dp(a-25, b-75))
            
            return mem[(a,b)]

        return dp(n, n)