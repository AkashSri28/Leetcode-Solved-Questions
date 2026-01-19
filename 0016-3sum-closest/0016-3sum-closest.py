class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        abs_diff = float('inf')
        ans = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                d = abs(target - s)
                if d < abs_diff:
                    abs_diff = d
                    ans = s
                
                if s > target:
                    k -= 1
                else:
                    j += 1

        return ans

        TC: O(n^2 + n)
        SC: O(1)


        