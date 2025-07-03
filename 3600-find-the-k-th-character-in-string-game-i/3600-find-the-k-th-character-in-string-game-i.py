class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            for ch in word:
                if ch == 'z':
                    word = word+'a'
                else:
                    word = word + chr(ord(ch)+1)

        return word[k-1]
        