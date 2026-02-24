class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i = j = 0
        # while i < len(s):
        #     while j < len(t) and t[j] != s[i]:
        #         j += 1
            
        #     if j == len(t):
        #         return False
            
        #     if s[i] != t[j]:
        #         return False

        #     i += 1
        #     j += 1

        # return True
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

        # TC: O(n)
        # SC: O(1)
        