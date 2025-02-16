class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0]*(2*n-1)
        used = [False]*(n+1)

        def backtrack(index):
            while index < len(res) and res[index] != 0:
                index += 1
            if index == len(res):
                return True

            for i in range(n, 0, -1):
                if used[i]:
                    continue
                if i == 1 or (index+i < len(res) and res[index+i] == 0):
                    used[i] = True
                    res[index] = i
                    if i > 1:
                        res[index+i] = i

                    if backtrack(index+1):
                        return True
                    
                    used[i] = False
                    res[index] = 0
                    if i > 1:
                        res[index+i] = 0

            return False

        backtrack(0)

        return res

        # TC: O(n^2)
        # SC: O(1)
        # Approach: For filling data is res, we can fill max value and check next value. If doesnt work then we need to backtrack
        