class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = (n*(n+1))//2
        s2 = 0
        num = m

        while num <= n:
            s2 += num
            num += m
                
        return s - 2*s2

        # k = n // m
        # return n * (n + 1) // 2 - k * (k + 1) * m

        # TC: O(m)
        # SC: O(1)
        # Approach: only find those numbers which are divisible by m and deduct from total sum

        