class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # i, n = 0, len(chalk)
        # while k >= chalk[i]:
        #     k -= chalk[i]
        #     i = (i+1)%n
        # return i
        i = 0
        total = sum(chalk)  #O(n)
        k = k%total
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0
        
                
        
        