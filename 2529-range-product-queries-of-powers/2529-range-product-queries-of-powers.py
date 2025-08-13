class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        i = 0
        state = []
        while n > 0:
            if n & 1 == 1:
                state.append(pow(2, i)%mod)
            i += 1
            n = n>>1

        # print(state)

        ans = []

        for (s, e) in queries:
            num = 1
            for i in range(s, e+1):
                num *= state[i]
                num %= mod
            ans.append(num)

        return ans

        # TC: O(q*32)
        # # SC: O(32)   Since state array will have max 32 values
        # Approach: To find number as power of 2, find all set bits in its binary representation.  