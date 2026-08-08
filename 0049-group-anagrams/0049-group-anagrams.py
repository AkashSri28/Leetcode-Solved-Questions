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

# TC: O(n*klogk)
# SC: O(n*k)
# Approach: we confirm if all strings are lowercase chars
# now to group them we need to find something common
# if two strings are anagrams, their sorted form will be same
# hence we will sort and check in dict mem
# for testing we will check with null string as well


        