class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0

        def backtrack(n, i):
            if n == 0:
                return True
    
            while 3**i <= n:
                n -= 3**i
                if backtrack(n, i+1):
                    return True
                n += 3**i
                i += 1
            return False

        return backtrack(n, i)
        