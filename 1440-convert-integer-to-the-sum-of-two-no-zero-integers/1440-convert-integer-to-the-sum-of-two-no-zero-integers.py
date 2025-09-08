class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]

        # TC: O(n)
        # SC: O(1)
        # Approach: From i to n-1, check all pairs and find a pair where 0 not present in any element from pair
        