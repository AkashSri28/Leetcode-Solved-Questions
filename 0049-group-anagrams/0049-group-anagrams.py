class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in mem:
                mem[sorted_s] = [s]
                continue
            mem[sorted_s].append(s)

        res = []
        for v in mem.values():
            res.append(v)

        return res



        