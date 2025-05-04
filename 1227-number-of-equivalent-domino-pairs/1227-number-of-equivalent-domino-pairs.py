class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mem = defaultdict(int)

        for pair in dominoes:
            u, v = sorted(pair)
            s = str(u)+""+str(v)
            mem[s] += 1

        ans = 0
        for val in mem.values():
            if val > 1:
                ans += (val*(val-1))//2

        return ans
        