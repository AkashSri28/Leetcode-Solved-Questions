class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mem = defaultdict(int)
        ans = []
        for i in range(10):
            j = i
            while j+10 <= len(s):
                sub_s = s[j:j+10]
                mem[sub_s] += 1

                if mem[sub_s] == 2:
                    ans.append(sub_s)

                j += 10

        return ans

        # TC: O(10*n)
        # SC: O(n)
        # Approach: there can 10 starting points from 0 to 9. For each starting point, check all the strings and store. Once the count reaches 2, add to ans.

        