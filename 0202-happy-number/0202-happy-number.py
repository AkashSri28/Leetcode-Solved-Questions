class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        seen.add(1)

        def find_n(num):
            new_n = 0
            while num > 0:
                d = num % 10
                num = num // 10
                new_n += d*d
            return new_n

        while True:
            seen.add(n)
            new_n = find_n(n)
            if new_n in seen:
                if new_n == 1:
                    return True
                return False

            n = new_n

        