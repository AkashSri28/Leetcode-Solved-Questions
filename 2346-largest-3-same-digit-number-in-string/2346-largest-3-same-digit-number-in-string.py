class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ""
        ans = -1

        n = len(num)
        mem = dict()

        for i in range(3):
            if num[i] not in mem:
                mem[num[i]] = 0
            mem[num[i]] += 1
            
        if len(mem) == 1 and int(num[i]) > ans:
            ans = int(num[i])

        for i in range(3, n):
            j = i-3
            if num[i] not in mem:
                mem[num[i]] = 0
            mem[num[i]] += 1

            mem[num[j]] -= 1
            if mem[num[j]] == 0:
                del mem[num[j]]

            if len(mem) == 1 and int(num[i]) > ans:
                ans = int(num[i])

        return "" if ans == -1 else str(ans)*3






        
        