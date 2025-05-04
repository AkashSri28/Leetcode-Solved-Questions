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

        # TC: O(n)
        # SC: O(1)
        # Approach: since the dominoes value is between 1 to 9, mem will be between 11 -> 99. We can use an array of size 100 and store count. There is a technique, number of pairs increase by v-1, if count is v currently
        