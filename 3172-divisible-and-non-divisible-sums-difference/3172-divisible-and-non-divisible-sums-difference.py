class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = (n*(n+1))//2
        s2 = 0

        for num in range(1, n+1):
            if num%m == 0:
                s2 += num

        return s - 2*s2

        