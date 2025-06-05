class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = dict()
        
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            parent[ch] = ch

        def find_parent(ch):
            while parent[ch] != ch:
                ch = parent[ch]
            return ch

        for ch1, ch2 in zip(s1, s2):
            p_ch1 = find_parent(ch1)
            p_ch2 = find_parent(ch2)

            if p_ch1 > p_ch2:
                parent[p_ch1] = p_ch2
            else:
                parent[p_ch2] = p_ch1

        ans = []
        for ch in baseStr:
            ans.append(find_parent(ch))

        return "".join(ans)

        