class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        on, en = (n + 1) // 2, n // 2
        om, em = (m + 1) // 2, m // 2
        return on * em + en * om


    # TC: O(1)
    # SC: O(1)
    # Approach: Alice will win when flowers in lane x and greater than y and vice versa. Count all possiblities when x is odd and greater and y is even and smaller
        