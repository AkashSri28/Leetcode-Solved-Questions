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

        # TC: O(n)
        # SC: O(1)
        # Approach: since we need pairs where sum has same parity. Sum can be even or odd, for even sum we need both elements either odd or both even. If we take either odd or even pair, all elements need to be odd or even pair. So count all odds and even numbers.
        # Second part, when we need to find alternate pattern, first number will always be included, so we keep adding new numbers and updating valid previous. This will help in finding longest alternate pair chain
        