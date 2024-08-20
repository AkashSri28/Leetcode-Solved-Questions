class Solution:
    def romanToInt(self, s: str) -> int:
        i, ans = len(s)-1, 0
        table = dict({
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        })
        while i >= 0:
            ch = s[i]
            ans += table[ch]
            if i-1 >= 0 and table[s[i-1]] < table[s[i]]:
                ans += (-1)*table[s[i-1]]
                i -= 1
            i -= 1
        return ans