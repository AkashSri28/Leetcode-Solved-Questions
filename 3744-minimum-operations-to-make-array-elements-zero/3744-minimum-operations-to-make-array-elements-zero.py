class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0

        def find_ops(q1, q2):
            s = 1
            L = 1
            R = 4*L - 1
            ops = 0
            while L <= q2:
                start = max(L, q1)
                end = min(R, q2)
                if start <= end:
                    ops += (end-start+1)*s
                # print(ops)
                L = L*4
                R = L*4 - 1
                s += 1
            return math.ceil(ops/2)

        for q in queries:
            ans += find_ops(q[0], q[1])
        return ans

        # TC: O(q*log4 r)
        # SC: O(1)
        # Approach: basically for numbers between (1,3) 1 operation is needed to convert to 0
        #                                         (4, 15) 2 operations needed
        #                                         (16, 63) 3 operations needed
        #                                         (4*L, 4*L-1) so we can move this range and check how many elements fall in this range
        #                                         range will be valid until (L <= r)

        