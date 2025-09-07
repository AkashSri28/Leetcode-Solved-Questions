class Solution:
    def sumZero(self, n: int) -> List[int]:
        start = n//2
        ans = []
        for i in range(start, 0, -1):
            ans.append(i)
            ans.append(-i)

        if n%2 == 1:
            ans.append(0)
        
        return ans




        