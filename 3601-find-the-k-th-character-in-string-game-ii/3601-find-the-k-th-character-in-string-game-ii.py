class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        idx = n
        shift = 0
        while idx > 0:
            idx -= 1
            half_length = 1 << idx  # Equivalent to 2^idx
            if k > half_length:
                k -= half_length
                if operations[idx] == 1:
                    shift += 1
            # If k <= half_length, we move to the first half without changing k
        # After processing all operations, apply the accumulated shifts
        ch_ord = (ord('a') - ord('a') + shift) % 26
        ch = chr(ch_ord + ord('a'))
        return ch
        