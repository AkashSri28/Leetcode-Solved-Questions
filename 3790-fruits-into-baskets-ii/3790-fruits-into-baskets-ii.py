class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        state = [0]*n

        for i in range(n):
            for j in range(n):
                if state[j] == 0 and fruits[i] <= baskets[j]:
                    state[j] = 1
                    break

        return n-sum(state)

        # TC: O(n^2)
        # SC: O(1)
        # Approach: For each fruit, we will check from left to right and whichever basket is unused, we will mark it used. Count unused baskets in the end.

        