class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(spells)
        n = len(potions)
        ans = [0]*m

        for i in range(m):
            low, high = 0, n-1
            sp = spells[i]
            while low <= high:
                mid = (low + high)//2
                pt = potions[mid]
                if sp* pt >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            ans[i] = n-(high+1)

        return ans

        