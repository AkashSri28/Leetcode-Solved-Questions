class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        num = 1
        n = abs(n)
        p = 1
        while num < n:
            num = pow(2, p)
            p += 1
        if num == n:
            return True
        return False