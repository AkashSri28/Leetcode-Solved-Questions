class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(op, ls):
            ans = ls[0]
            if op == '!':
                ans = not(ans)
            elif op == '&':                
                for i in range(1, len(ls)):
                    ans = ans and ls[i]
            else:
                for i in range(1, len(ls)):
                    ans = ans or ls[i]
            return ans
        
        stack = []
        for i in expression:
            if i == ',':
                continue
            elif i == ')':
                ls = []     #list of operands
                while stack[-1] != '(':
                    ch = stack.pop()
                    ls.append(ch)
                    
                stack.pop()
                op = stack.pop()
                res = evaluate(op, ls)
                stack.append(res)
            else:
                if i == 'f':
                    stack.append(False)
                elif i == 't':
                    stack.append(True)
                else:
                    stack.append(i)
                
        return stack[-1]
        