class Solution:
    def minimumSteps(self, s: str) -> int:
        # s = list(s)
        j = ans = 0
        for i in range(len(s)):
            if s[i] == '0':
                ans += (i-j)
                # s[i], s[j] = s[j], s[i]
                j += 1
                
        return ans
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: Find white ball and swap with its correct location. Find difference in its position before and after swap.