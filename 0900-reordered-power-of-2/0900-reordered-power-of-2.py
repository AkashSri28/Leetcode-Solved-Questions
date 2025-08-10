class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        num = 0
        n1 = ''.join(sorted(str(n)))
        print(n1)

        for i in range(31):
            num = pow(2, i)
            num1 = ''.join(sorted(str(num)))
            print(num1)
            if num1 == n1:
                return True
        return False

        # TC: O(dlogd*31)
        # SC: O(d)
        # Approach: to compare 2 numbers we can check their sorted representations.

        