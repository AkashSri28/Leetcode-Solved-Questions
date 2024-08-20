class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brac = set(['(', '{', '['])
        close_brac = set([')', '}', ']'])
        
        def valid(op, cl):
            if (op == '(' and cl == ')') or (op == '{' and cl == '}') or (op == '[' and cl == ']'):
                return True
            return False
            
        for ch in s:
            if ch in open_brac:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if not valid(temp, ch):
                        return False
        if len(stack) == 0:
            return True
        return False
        