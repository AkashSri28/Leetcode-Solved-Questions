class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        one_count = [0]*(n+1)
        for i in range(1, n+1):
            one_count[i] = one_count[i-1] + int(s[i-1])

        total_ones = one_count[n]

        ans = float('-inf')

        for i in range(1, n):
            left_count = i - one_count[i]
            right_count = total_ones - one_count[i]
            ans = max(ans, left_count + right_count)

        return ans

        