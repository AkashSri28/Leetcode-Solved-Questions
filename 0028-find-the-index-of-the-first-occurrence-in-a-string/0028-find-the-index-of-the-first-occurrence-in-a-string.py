class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1

        j = len(needle)
        i = 0
        while j <= len(haystack):
            s = haystack[i:j]
            if s == needle:
                return i
            i += 1
            j += 1
        return -1


