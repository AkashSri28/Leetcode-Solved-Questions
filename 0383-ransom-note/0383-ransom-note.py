class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_freq, m_freq = [0]*26, [0]*26

        def freq_counter(freq, s):
            for ch in s:
                ch_ind = ord(ch) - ord('a')
                freq[ch_ind] += 1

        freq_counter(r_freq, ransomNote)
        freq_counter(m_freq, magazine)

        for i in range(26):
            if m_freq[i] < r_freq[i]:
                return False

        return True
        