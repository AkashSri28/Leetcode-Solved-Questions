class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # ans = 0
        # def helper(index, cnt, n):
        #     nonlocal ans
        #     if index == len(s):
        #         ans = max(ans, cnt)
        #         return
        #     num = (n*2)+int(s[index])
        #     if num <= k:
        #         helper(index+1, cnt+1, num)
        #     helper(index+1, cnt, n)

        # helper(0, 0, 0)
        # return ans

        cnt = 0
        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                cnt += 1
            else:
                num = 1<<cnt
                if num <= k:
                    k -= num
                    cnt += 1
        return cnt

        