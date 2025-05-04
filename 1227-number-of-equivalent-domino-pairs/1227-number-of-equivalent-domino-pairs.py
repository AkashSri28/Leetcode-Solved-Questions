class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mem = [0]*100
        ans = 0
        for pair in dominoes:
            u, v = sorted(pair)
            s = 10*u + v
            mem[s] += 1
            ans += (mem[s]-1)

        return ans
        