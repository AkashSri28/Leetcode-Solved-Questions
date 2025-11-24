class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = [0]*26
        q = deque()
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            seen[idx] += 1
            if seen[idx] == 1:
                q.append(i)
            
        
        while q and seen[ord(s[q[0]]) - ord('a')] > 1:
            q.popleft()

        return q[0] if q else -1

        # TC: O(n)
        # SC: O(1)
        # Approach: store elements in array along with freq, now pop elements with freq > 1. Top element will be answer



                