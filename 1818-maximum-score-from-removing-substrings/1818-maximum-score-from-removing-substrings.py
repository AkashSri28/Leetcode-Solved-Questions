class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        ans = 0

        s1, s2 = "ab", "ba"
        if y > x:
            s1, s2 = s2, s1

        def find_score(s1, x):
            nonlocal s
            stack = []
            res = 0
            for ch in s:
                if stack and stack[-1]+ch == s1:
                    res += x
                    stack.pop()
                    continue
                stack.append(ch)
            s = ''.join(stack)
            return res

        ans += find_score(s1, max(x, y))
        ans += find_score(s2, min(x, y))

        return ans

        # TC: O(n)
        # SC: O(n)
        # Approach: We can remove ab in 1st iteration and ba in 2nd iteration. If y is greater than x then remove ba first and ab next
        