class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = [0]*26
        q = deque()
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if seen[idx] == 0:
                q.append(i)
            seen[idx] += 1
        
        while q and seen[ord(s[q[0]]) - ord('a')] > 1:
            q.popleft()

        return q[0] if q else -1



                