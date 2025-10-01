class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        rem = 0

        while numBottles > 0:
            # print(numBottles)
            ans += numBottles 
            numBottles += rem
            rem = numBottles % numExchange
            numBottles = numBottles // numExchange
        return ans
            


        