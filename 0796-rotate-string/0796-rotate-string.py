class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        return goal in s+s
        
        
#         indices = []
#         c = s[0]
#         n = len(s)
        
#         def check(i):
#             for ch in s:
#                 if goal[i] != ch:
#                     return False
#                 i = (i+1)%n
#             return True
                    
#         for index, ch in enumerate(goal):
#             if ch == c:
#                 indices.append(index)
                
#         for i in indices:
#             if check(i):
#                 return True
#         return False
    
    # TC: O(n) + O(n) Finding indices and checking strings
    #     SC: O(n)    Storing indices
    #         Approach: Find all occurance of starting char and check if the string matches.
        