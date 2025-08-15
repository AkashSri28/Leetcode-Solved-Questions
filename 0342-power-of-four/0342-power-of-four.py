class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]

        # TC: O(1)
        # SC: O(1)
        # Approach: Find all powers of 4 before and store. Now check if n exists there
        