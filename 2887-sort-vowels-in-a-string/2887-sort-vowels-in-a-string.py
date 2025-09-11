class Solution:
    def sortVowels(self, s: str) -> str:
        s1 = "AEIOUaeiou"
        mem = []
        chars = list(s)
        for ch in chars:
            if ch in s1:
                mem.append(ch)

        print(mem)
        mem.sort()

        j = 0
        for i, ch in enumerate(chars):
            if ch in s1:
                chars[i] = mem[j]
                j += 1

        return ''.join(chars)


        

        