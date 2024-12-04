class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or ord(str2[j]) - ord(str1[i]) == 1 or ord(str2[j]) - ord(str1[i]) == -25:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(str2):
            return True
        return False
    
    # TC: O(len(str2))
    #     SC: O(1)
    #         Approach: each character which can be used, we will include it and pass others
        