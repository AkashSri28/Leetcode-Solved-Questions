class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freq, even_freq = 0, float('inf')
        for val in freq.values():
            if val%2 == 1:
                odd_freq = max(odd_freq, val)
            else:
                even_freq = min(even_freq, val)

        # if even_freq == float('inf'):
        #     even_freq = 0

        return odd_freq-even_freq

        