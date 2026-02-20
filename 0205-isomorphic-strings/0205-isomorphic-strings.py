class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mem1, mem2 = {}, {}
        for char_s, char_t in zip(s, t):
            if char_s not in mem1 and char_t not in mem2:
                mem1[char_s] = char_t
                mem2[char_t] = char_s

            else:
                if (char_s in mem1 and mem1[char_s] != char_t) or (char_t in mem2 and mem2[char_t] != char_s):
                    return False

        return True

        