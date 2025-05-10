class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = z2 = 0

        for n in nums1:
            if n == 0:
                z1 += 1 

        for n in nums2:
            if n == 0:
                z2 += 1

        n1_sum, n2_sum = sum(nums1)+z1, sum(nums2)+z2

        if z1 == 0 and n2_sum > n1_sum:
            return -1

        if z2 == 0 and n1_sum > n2_sum:
            return -1

        return max(n1_sum, n2_sum)

        # TC: O(n)
        # SC: O(n)
        # Approach: min sum will equal to curr sum + 0 count. Find scenario where both cant reach this value
        