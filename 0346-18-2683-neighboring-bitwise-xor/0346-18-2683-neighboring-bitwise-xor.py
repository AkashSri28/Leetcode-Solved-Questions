class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0
        for num in derived:
            xor ^= num

        if xor == 0:
            return True
        return False

        # TC: O(n)
        # SC: O(1)
        # Approach: if the xor of all numbers is 0, it means that for every number internally there existed a pair
        