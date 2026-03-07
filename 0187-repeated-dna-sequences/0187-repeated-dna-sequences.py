class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mem = defaultdict(int)
        ans = []
        i = 0
        while i+10 <= len(s):
            sub_s = s[i:i+10]
            mem[sub_s] += 1

            if mem[sub_s] == 2:
                ans.append(sub_s)

            i += 1

        return ans

        # TC: O(10*n)
        # SC: O(n)
        # Approach: there can 10 starting points from 0 to 9. For each starting point, check all the strings and store. Once the count reaches 2, add to ans.

        