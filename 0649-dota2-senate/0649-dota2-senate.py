class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q_r = deque()
        q_d = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                q_r.append(i)
            else:
                q_d.append(i)

        while q_r and q_d:
            r = q_r.popleft()
            d = q_d.popleft()
            if r < d:
                q_r.append(r+n)
            else:
                q_d.append(d+n)

        if q_r:
            return "Radiant"
        return "Dire"    

        