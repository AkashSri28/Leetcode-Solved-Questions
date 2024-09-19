class Solution:
    operators = {
        '+': lambda x, y: x+y,
        '*': lambda x, y: x*y,
        '-': lambda x, y: x-y
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        for i in range(len(expression)):
            ch = expression[i]
            if ch in self.operators:
                nums1 = self.diffWaysToCompute(expression[:i])
                nums2 = self.diffWaysToCompute(expression[i+1:])
                
                for n1 in nums1:
                    for n2 in nums2:
                        res.append(self.operators[ch](n1, n2))
                        
        if not res:
            res.append(int(expression))
                
        
        return res
    
    #TC: O(2^n+n)       #2^n for string of len n, 2 subtrees will be created at each step, for find res O(n) 
    #SC: O(2^n)         #Recursion tree can go to depth 2^n
    #Approach:          #For every operator we can split expression and check until we reach base case. Base case is when dont have any operator in expression
        