class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o, c, curr):
            if o == 0 and c == 0:
                res.append(''.join(curr))
            if o > 0:
                curr.append('(')
                backtrack(o-1, c, curr)
                curr.pop()
            if c > o:
                curr.append(')')
                backtrack(o, c-1, curr)
                curr.pop()
            

        backtrack(n, n, [])
        return res
        