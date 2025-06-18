class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        i = 0
        while i < n:
            if nums[i+2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
            i = i+3
        
        return ans

        # TC: O(nlogn)
        # SC: O(n)    TimSort needs O(n) space
        # Approach: To minimise the difference sort array, and check difference of 1st and last element in triplet 

        