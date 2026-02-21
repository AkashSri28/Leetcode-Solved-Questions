class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = defaultdict(list)
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     mem[sorted_word].append(word)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            mem[tuple(count)].append(word)

        # ans = []

        # for v in mem.values():
        #     ans.append(v)

        # return ans
        return list(mem.values())

        # TC: O(n*mlogm)
        # SC: O(n*m)

        