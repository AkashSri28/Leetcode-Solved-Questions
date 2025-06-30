class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for k in freq.keys():
            if k+1 in freq:
                ans = max(ans, freq[k]+freq[k+1])

        return ans

        # TC: O(n)
        # SC: O(n)
        # Approach: so we need sequence with harmonious number = 1. This means we need only those elements in n with difference 1. So if we take count of num and num+1, that will be length of harmonious sequence

