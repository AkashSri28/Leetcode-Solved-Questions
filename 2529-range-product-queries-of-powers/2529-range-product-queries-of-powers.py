class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        bin = []
        while n >= 2:
            bin.append(n%2)
            n //= 2
        
        bin.append(n)
        # print(bin)
        
        state = [1]
        for i in range(len(bin)):
            if bin[i] == 1:
                state.append(pow(2, i)%mod)
                state[-1] = (state[-1]*state[-2])%mod

        ans = []

        for (s, e) in queries:
            num = state[e+1] * pow(state[s], mod-2, mod) % mod
            # print(num)
            ans.append(num)

        return ans