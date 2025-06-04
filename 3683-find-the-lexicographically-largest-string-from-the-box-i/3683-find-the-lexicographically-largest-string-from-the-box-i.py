class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        curr = ""
        for i in range(n):
            tmp = word[i:min(i+n+1-numFriends, n)]
            curr = max(curr, tmp)

        return curr


        