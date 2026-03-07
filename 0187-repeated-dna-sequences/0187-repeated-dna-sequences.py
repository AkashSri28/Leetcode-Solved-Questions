class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        ans = set()
        i = 0
        while i+10 <= len(s):
            sub_s = s[i:i+10]
            if sub_s in seen:
                ans.add(sub_s)

            seen.add(sub_s)
            i += 1
        return list(ans)

        # TC: O(n)
        # SC: O(n)
        # Approach: there can 10 starting points from 0 to 9. For each starting point, check all the strings and store. Once the count reaches 2, add to ans. If frequency not required then use set and not hashmap.

        