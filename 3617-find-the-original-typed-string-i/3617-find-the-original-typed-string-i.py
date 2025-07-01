class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                ans += 1

        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: in abbcccc, ab_c___ is fixed. We have 4 places to fill and we can skip 1 place at a time. Therefore, we have 4 choices here. Also, we can include original word. So total choices 4+1 = 5
        