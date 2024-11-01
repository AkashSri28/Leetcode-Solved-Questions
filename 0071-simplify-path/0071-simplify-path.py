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
                
        return '/'+'/'.join(stack)\
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: Find all folders and remove empty name folders. Now if we see .. and stack has something, pop. if we see . just ignore. if we see anything else, push on stack. Merge stack in the end.
        