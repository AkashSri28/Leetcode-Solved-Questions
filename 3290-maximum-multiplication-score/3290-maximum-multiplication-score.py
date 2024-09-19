class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = 4, len(b)
        # Memoization dictionary to store intermediate results
        memo = {}

        def max_score(i, j):
            # If we need to pick 0 elements, the score is 0
            if i == 0:
                return 0
            # If there are not enough elements in b to pick i elements, return negative infinity
            if j < i:
                return -float('inf')
            # If this subproblem has been solved, return the cached result
            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: Skip the current element in `b`
            option1 = max_score(i, j - 1)

            # Option 2: Pick the current element in `b`
            option2 = max_score(i - 1, j - 1) + a[i - 1] * b[j - 1]

            # Store the result in memo
            memo[(i, j)] = max(option1, option2)
            return memo[(i, j)]

        # The result is the maximum score using all 4 elements of `a`
        return max_score(m, n)
        
        
#         m, n = len(b), len(a)
#         dp = [[-float('inf')]*n for _ in range(m)]

#         def func(i, j):
#             if j == n:
#                 return 0
#             if i == m:
#                 return -(10**6)
            
#             if dp[i][j] == -float('inf'):
#                 dp[i][j] = b[i]*a[j] + func(i+1, j+1)
#                 if i<m:
#                     dp[i][j] = max(dp[i][j], func(i+1, j))

#             return dp[i][j]

#         return func(0, 0)
        