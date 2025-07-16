class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_odd = count_even = 0
        prev = nums[0]
        cnt = 1
        for num in nums:
            if num%2 == 1:
                count_odd += 1
            else:
                count_even += 1
            if (prev+num)%2 == 1:
                prev = num
                cnt += 1 

        return max(count_odd, count_even, cnt)
        