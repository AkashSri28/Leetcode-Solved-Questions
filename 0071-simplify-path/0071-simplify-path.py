class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split('/')
        folders = [f for f in folders if f]
        stack = []
        
        for f in folders:
            if f == '..':
                if stack:
                    stack.pop()
            elif f == '.':
                continue
            else:
                stack.append(f)
                
        return '/'+'/'.join(stack)
        