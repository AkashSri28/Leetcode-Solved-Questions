class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        i = 0
        state = [1]
        while n > 0:
            if n & 1 == 1:
                state.append(pow(2, i))
                state[-1] *= state[-2]
            i += 1
            n = n>>1

        print(state)

        ans = []

        for (s, e) in queries:
            num = state[e+1] * pow(state[s], mod-2, mod) % mod
            # print(num)
            ans.append(num)

        return ans