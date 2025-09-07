class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            val = num1 - i*num2
            if val.bit_count() <= i <= val:
                return i
            if val < 0:
                return -1
        return -1

        # TC: O(1)
        # SC: O(1)
        # Approach: num1' = num1 - num2 - 2^i
        #           num1'' = num1' - num2 - 2^i
        #           num1''' = num1'' - num2 - 2^i
        #                 = num1' - num2 - 2^i - num2 - 2^i
        #                 = num1 - num2 - 2^i- num2 - 2^i - num2 - 2^i
        #                 = num1 - 3*num2 - (2^i + 2^j + 2^k)
        #         now if we want to make num1''' as 0
        #         0 = num1 - 3*num2 - (2^i + 2^j + 2^k)
        #         (2^i + 2^j + 2^k) = num1 - t*num2

        #         so we take value of t from 1 to 60 and check when number of 2^i terms are suitable
        #         min will be number of set bits, max will be val (2^0, sum of all 1s), so if our value lies between this then we have answer


        
        