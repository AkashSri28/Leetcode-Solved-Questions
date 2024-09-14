class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # MAX = max(nums) ### Find the largest number in nums.
        # res = 0			 
        # count = 0		### Used to count the length of the continues subarray that only contains MAX
        # for n in nums:
        # 	### If the current number is MAX, increase count
        #     if n==MAX:
        #         count +=1
        #     ### Otherwise, reset count.
        #     else:
        #         count = 0
        #     ### store the maximum count as result.
        #     res = max(res, count)
        # return res
        n = len(nums)
            
        maxi, cnt, ans = nums[0], 1, 1
        
        for i in range(1, n):
            if maxi == nums[i]:
                cnt += 1
                ans = max(ans, cnt)
            elif maxi < nums[i]:
                maxi = nums[i]
                cnt = 1
                ans = 1
            else:
                cnt = 0
                
        return ans

            
        
        
            
        