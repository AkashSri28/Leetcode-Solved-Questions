class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def digit_sum(s, left, right):
            s_sum = 0
            for i in range(left, right+1):
                s_sum += int(s[i])
            return s_sum

        cnt = 0
        for num in range(low, high+1):
            s = str(num)
            l = len(s)
            if l%2 != 0:
                continue
            mid = l//2
            left_sum = digit_sum(s, mid, l-1)
            right_sum = digit_sum(s, 0, mid-1)

            if left_sum == right_sum:
                cnt += 1
        return cnt


        