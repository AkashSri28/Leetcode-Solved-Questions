class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n, i = [], len(nums), 0
        nums.sort()
        while i < n-2:
            j, k = i+1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    
            while i+1 < n and nums[i+1] == nums[i]:
                i += 1
            
            i += 1
        
        return ans
        
# TC: O(n^2)  #O(n) for i, and O(n) for finding 2 sum using j and k
#     SC: O(n)    #storing result
#         Approach: fix 1 element, now we can adjust 2 other pointers until sum becomes 0. Moving j will increase sum and moving k will decrease sum