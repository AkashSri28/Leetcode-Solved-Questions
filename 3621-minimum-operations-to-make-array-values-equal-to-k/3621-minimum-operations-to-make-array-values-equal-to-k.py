class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        s.add(k)

        for num in nums:
            if num not in s:
                s.add(num)

        s = list(s)
        s.sort()

        if s[0] != k:
            return -1

        return len(s) - 1