class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # num = 1
        # while num < n:
        #     num *= 3
        # return num == n

        MAX_POWER_OF_3 = 1162261467
        return n > 0 and MAX_POWER_OF_3 % n == 0

        # TC: O(log3 n)
        # SC: O(1)
        # Approach: Take number num and keep multiplying it with 3 until num < n. Once num reaches n, check if num == n, else return False

        