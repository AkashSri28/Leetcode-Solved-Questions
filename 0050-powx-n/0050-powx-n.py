class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n < 0:
            neg = True
            n = -n
        ans = 1
        while n > 0:
            if n%2 == 1:
                ans *= x
                n = n-1
            else:
                x = (x*x)
                n = n//2
        if neg:
            return 1/ans
        return ans
    
    # TC: O(log n)
    #     SC: O(1)
    #         Approach: 2**9 can be represented as 2 x 2**4 x 2**4
        
        