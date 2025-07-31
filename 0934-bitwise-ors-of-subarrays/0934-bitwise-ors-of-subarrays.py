class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for num in arr:
            new_cur = {num}
            for val in cur:
                new_cur.add(num | val)
            cur = new_cur
            res.update(cur)

        return len(res)
        