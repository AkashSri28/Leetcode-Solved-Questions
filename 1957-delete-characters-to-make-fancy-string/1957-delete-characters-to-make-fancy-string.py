class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for ch in s:
            # Check if the last two characters in the result are the same as the current character
            if len(result) >= 2 and result[-1] == ch and result[-2] == ch:
                continue  # Skip the character if it would make three consecutive characters
            result.append(ch)

        return ''.join(result)
        # n = len(s)
        # new_s = ""
        # for i in range(n):
        #     if i >= 2 and s[i] == s[i-1] and s[i] == s[i-2]:
        #         continue
        #     new_s = new_s + s[i]
        # return new_s
    
    # TC: O(n)
    #     SC: O(1)
    #         Approach: we can skip those chars which are seen on last 2 occasions
        