class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        used = [False]*26
        left = [0]*26

        for ch in s:
            left[ord(ch)-ord('a')] += 1

        stack = []
        for ch in s:
            if used[ord(ch)-ord('a')]:
                left[ord(ch)-ord('a')] -= 1
                continue
                
            while stack and stack[-1] > ch and left[ord(stack[-1])-ord('a')] > 0:
                used[ord(stack[-1])-ord('a')] = False
                stack.pop()

            stack.append(ch)
            left[ord(ch)-ord('a')] -= 1
            used[ord(ch)-ord('a')] = True

        return ''.join(stack)

        

        