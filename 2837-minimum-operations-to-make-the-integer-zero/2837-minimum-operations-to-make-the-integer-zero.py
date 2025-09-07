class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 61):
            val = num1 - i*num2
            if val.bit_count() <= i <= val:
                return i
            if val < 0:
                return -1
        return -1

        
        