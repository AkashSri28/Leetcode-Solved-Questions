class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        bLList = list(brokenLetters)

        for word in text.split():
            cnt += 1
            for l in bLList:
                if l in word:
                    cnt -= 1
                    break
        
        return cnt
        