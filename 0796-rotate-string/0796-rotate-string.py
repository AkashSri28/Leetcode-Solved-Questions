class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        indices = []
        c = s[0]
        n = len(s)
        
        def check(i):
            for ch in s:
                if goal[i] != ch:
                    return False
                i = (i+1)%n
            return True
                    
        for index, ch in enumerate(goal):
            if ch == c:
                indices.append(index)
                
        for i in indices:
            if check(i):
                return True
        return False
        