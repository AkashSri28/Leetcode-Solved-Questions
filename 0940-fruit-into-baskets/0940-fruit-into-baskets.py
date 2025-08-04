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

        # TC: O(n)
        # SC: O(1)
        # Approach: we need to find longest subarray where at most 2 distinct elements are present. So we count frequency of elements and once frequency exceeds 2, we start moving other pointer (which is j) untill freq <= 2. i-j+1 will give current element count

        