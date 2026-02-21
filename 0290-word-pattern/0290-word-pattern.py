class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_list = s.split()
        if len(pattern) != len(word_list):
            return False

        mem1, mem2 = {}, {}

        for ch, word in zip(pattern, word_list):
            if ch in mem1:
                if mem1[ch] != word:
                    return False

            else:
                if word in mem2:
                    return False

                mem1[ch] = word
                mem2[word] = ch

        return True

        # TC: O(n+n)
        # SC: O(n+n+n)
        