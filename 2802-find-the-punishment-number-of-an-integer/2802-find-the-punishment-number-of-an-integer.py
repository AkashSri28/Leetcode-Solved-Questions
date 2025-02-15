class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        def partition(curr, rem, target):
            if rem == 0 and curr == target:
                return True
            
            m = 1
            while m <= rem:
                if partition(curr + rem//m, rem%m, target):
                    return True
                m *= 10

            return False

        for i in range(1, n+1):
            target = i*i
            if partition(0, target, i):
                ans += target

        return ans

        # TC: O(n*k)
        # SC: O(1)
        # Apporach: Break a number in subparts and check subpart sum. If sum is equal to target return true


        