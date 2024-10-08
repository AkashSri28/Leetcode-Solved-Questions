class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2

#         stack = []
#         for ch in s:
#             if ch == ']' and stack and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(ch)
                
#         return len(stack)//2

                
                
        