class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = (n*(n+1))//2
        s2 = 0
        num = m

        while num <= n:
            s2 += num
            num += m
                
        return s - 2*s2

        