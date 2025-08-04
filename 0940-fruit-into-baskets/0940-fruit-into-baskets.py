class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mem = dict()
        j = ans = 0

        for i in range(n):
            if fruits[i] not in mem:
                mem[fruits[i]] = 1
            else:
                mem[fruits[i]] += 1
                
            while j < n and len(mem) > 2:
                mem[fruits[j]] -= 1
                if mem[fruits[j]] == 0:
                    del mem[fruits[j]]
                j += 1
            ans = max(ans, i-j+1)

        return ans

        