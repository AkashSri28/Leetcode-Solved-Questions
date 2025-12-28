class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q_r = deque()
        q_d = deque()
        n = len(senate)
        for i, ch in enumerate(senate):
            if ch == 'R':
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

        return "Radiant" if q_r else "Dire"

        # TC: O(2n)
        # SC: O(2n)
#         Approach: You store the indices of R and D senators in two queues.

# In each round, the senator with the smaller index acts first and bans the other.

# The winner gets re-added with index + n to simulate them coming back in the next cycle.

# Loop ends when one party has no senators left.

        