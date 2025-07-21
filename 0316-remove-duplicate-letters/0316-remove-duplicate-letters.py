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

        # TC: O(n)
        # SC: O(n)
        # Approach: since we need to maintain increasing order we will use montonic array. Now we need to check some conditions before popping element from stack. It should occur in future, else it will be lost forever. For that we use left array. Also we cant use duplicate element in monotonic stack, so we use used array to remember already used element


        

        