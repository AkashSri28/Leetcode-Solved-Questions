class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()

        for num in arr:
            curr = set()
            for p in prev:
                curr.add(p|num)
            curr.add(num)
            res.update(curr)
            prev = curr

        return len(res)

        # TC: O(n*32)
        # SC: O(32)
        # Approach: For curr number, we can Or it with Or of all prev results. And store unique values, in worst cast 32 values will be stored. So the solution will be sufficient
