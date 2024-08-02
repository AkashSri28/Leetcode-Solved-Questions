class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_one =  nums.count(1)
        n = len(nums)
        count_zero_window = 0
        res = 0
        
        for i in range(count_one):
            if nums[i] == 0:
                count_zero_window += 1
                
        res = count_zero_window
        
        for i in range(0, n - 1):
            j = (i + count_one)%n
            if nums[i] == nums[j]:
                continue
            if nums[i] == 0:
                count_zero_window -= 1
            if nums[j] == 0:
                count_zero_window += 1
            res = min(res, count_zero_window)
            
        return res
            
            
    # TC: O(n)
    #     SC: O(1)
    #         Approach: maximum 1s consecutive can stay in window of size == count of 1 in array. Now remove 1 element and add one element to check if we find a window with minimum 0 count
        