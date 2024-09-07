class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 0
        p = math.floor(math.log(n, 5))
        for i in range(1, p+1):
            num = 5**i
            ans += (n//num)
        return ans
        