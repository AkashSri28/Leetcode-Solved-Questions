class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        first_index, last_index = dict(), dict()
        
        for i in range(n):
            if nums[i] not in first_index:
                first_index[nums[i]] = i

        for i in range(n-1, -1, -1):
            if nums[i] not in last_index:
                last_index[nums[i]] = i

        ans = 0

        for key in first_index.keys():
            if key+1 in last_index:
                ans = max(ans, last_index[key+1]-first_index[key]+1)

        return ans