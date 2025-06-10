class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # if sum(gas) < sum(cost):
        #     return -1

        # def check(i):
        #     j, m = (i+1)%n, gas[i] - cost[i]
        #     while j != i:
        #         m += (gas[j] - cost[j])
        #         if m < 0:
        #             break
        #         j = (j+1)%n
            
        #     return j

        # i = 0
        # while i < n:
        #     diff = gas[i] - cost[i]
        #     if diff < 0:
        #         i += 1
        #         continue
        #     if check(i) == i:
        #         return i
        #     elif check(i) > i:
        #         i = check(i)+1
        #     else:
        #         return -1

        # return -1
        total_tank = 0   # Total gas in the system
        curr_tank = 0    # Gas in the tank for current journey
        start = 0        # Candidate starting station

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # If we can't reach the next station
            if curr_tank < 0:
                # Start from the next station
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1

        