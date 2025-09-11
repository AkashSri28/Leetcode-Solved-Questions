class Solution:
    def sortVowels(self, s: str) -> str:
        s1 = set("AEIOUaeiou")
        mem = []
        chars = list(s)
        for ch in chars:
            if ch in s1:
                mem.append(ch)

        mem.sort()

        j = 0
        for i, ch in enumerate(chars):
            if ch in s1:
                chars[i] = mem[j]
                j += 1

        return ''.join(chars)

        # TC: O(2n+nlogn)
        # SC: O(n)
        # Approach: in one iteration find all vowels, in second iteration, replace vowels with lowest ascii value vowel (stored in mem)


        

        