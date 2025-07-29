class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits = [0]*30
        n = len(nums)
        ans = [1]*n

        for i in range(n-1, -1, -1):
            num = nums[i]
            pos = 0
            while num > 0:
                if num & 1:
                    bits[pos] = i
                num = num >> 1
                pos += 1
            ans[i] = max(ans[i], max(bits) - i + 1)

        return ans

        # TC: O(n*30)
        # SC: O(n)
        # Approach: we need to calculate max or from right to left. Keep storing closest set bit position. For every number farthest bit position will be the minimum subarray needed to find max or
        