class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        new_s = []
        for i in range(n):
            if i >= 2 and s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            new_s.append(s[i])
        return ''.join(new_s)
    
    # TC: O(n)
    #     SC: O(1)
    #         Approach: we can skip those chars which are seen on last 2 occasions
        