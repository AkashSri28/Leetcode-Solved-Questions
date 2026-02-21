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

        while n != 1 and n not in seen:
            seen.add(n)
            n = find_n(n)

        return n == 1

        # TC: O(n*d)
        # SC: O(n)
        # Approach: check for cycle, if we reach 1 or cycle, break from loop. If 1 return True, else False