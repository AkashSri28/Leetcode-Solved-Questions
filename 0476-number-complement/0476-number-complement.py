class Solution:
    def findComplement(self, num: int) -> int:
        n = math.log(num, 2)
        n = math.floor(n)+1
        ans = (2**n - 1) - num
        return ans