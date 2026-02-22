class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # if n == 0:
        #     return 0

        # nums.sort()
        # ans = cnt = 1
        # for i in range(1, n):
        #     if nums[i] == nums[i-1]+1:
        #         cnt += 1
        #         ans = max(ans, cnt)
        #     elif nums[i] == nums[i-1]:
        #         continue
        #     else:
        #         cnt = 1

        # return ans

        # TC: O(nlogn)
        # SC: O(1)
        # Approach: sort and check, skip duplicates

        # Better solution
        nums_set = set(nums)
        ans = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                while num+1 in nums_set:
                    cnt += 1
                    num += 1
                ans = max(ans, cnt)

        return ans

        # TC: O(n)
        # SC: O(n)
        # Approach: store all nums in a set. Now for each element in a set, check if its starting point num-1 will not be in set. Count until num+1 is in set.


        