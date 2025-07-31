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

