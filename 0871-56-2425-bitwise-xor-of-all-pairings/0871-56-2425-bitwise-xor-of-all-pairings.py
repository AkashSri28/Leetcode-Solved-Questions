class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1_xor = num2_xor = 0
        if len(nums2)%2 != 0:
            for num in nums1:
                num1_xor ^= num 
        if len(nums1)%2 != 0:
            for num in nums2:
                num2_xor ^= num

        return num1_xor^num2_xor

        # TC: O(n+m)
        # SC: O(1)
        # Apporach: even number of occurances will cancel out

        