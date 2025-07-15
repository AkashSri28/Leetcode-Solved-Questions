class Solution:
    def isValid(self, word: str) -> bool:
        v, c = False, False
        if len(word) < 3:
            return False
        for ch in word:
            if not ch.isdigit() and not ch.isalpha():
                return False
            if ch.isalpha():
                if ch in 'aeiou' or ch in 'AEIOU':
                    v = True
                else:
                    c = True
        return (v and c)

        # TC: O(n)
        # SC: O(1)
            
            

        