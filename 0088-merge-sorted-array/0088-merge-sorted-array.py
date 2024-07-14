class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        
        i, j = 0, m
        while i < m and j < m+n:
            if nums1[i] > nums1[j]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                k = j+1
                while k < m+n and temp > nums1[k]:
                    nums1[k-1] = nums1[k]
                    k += 1
                nums1[k-1] = temp   
            i += 1 
        
# TC: O(m*n)
# SC: O(1)
    