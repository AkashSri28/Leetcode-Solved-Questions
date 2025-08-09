class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        num = 1
        p = 1
        while num < n:
            num = pow(2, p)
            p += 1
        return num == n

        # TC: O(logn)
        # SC: O(1)
        # Approach: we take a num abd raise it to power p (0,1,2,3....) until we reach n. This will take logn time. Once we reach >= n, we can check if num == n