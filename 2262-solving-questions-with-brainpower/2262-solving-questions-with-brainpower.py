class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        mem = [-1]*n

        def dp(idx):
            if idx >= n:
                return 0
            if mem[idx] == -1:
                pts, bp = questions[idx]
                a = pts + dp(idx+bp+1)
                b = dp(idx+1)
                mem[idx] = max(a, b)

            return mem[idx]

        return dp(0)
        