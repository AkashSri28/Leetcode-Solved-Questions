from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def can_make_24(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS
            # Try all unordered pairs (i, j), i != j
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    # Build the next list without i and j
                    next_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    a, b = nums[i], nums[j]

                    # For + and * (commutative), we can enforce i < j to cut duplicates.
                    # But since we loop both i, j, we can still try all; small input keeps it fast.

                    # 1) a + b
                    next_nums.append(a + b)
                    if can_make_24(next_nums):
                        return True
                    next_nums.pop()

                    # 2) a - b
                    next_nums.append(a - b)
                    if can_make_24(next_nums):
                        return True
                    next_nums.pop()

                    # 3) b - a
                    next_nums.append(b - a)
                    if can_make_24(next_nums):
                        return True
                    next_nums.pop()

                    # 4) a * b
                    next_nums.append(a * b)
                    if can_make_24(next_nums):
                        return True
                    next_nums.pop()

                    # 5) a / b
                    if abs(b) > EPS:
                        next_nums.append(a / b)
                        if can_make_24(next_nums):
                            return True
                        next_nums.pop()

                    # 6) b / a
                    if abs(a) > EPS:
                        next_nums.append(b / a)
                        if can_make_24(next_nums):
                            return True
                        next_nums.pop()

            return False

        return can_make_24([float(x) for x in cards])

        