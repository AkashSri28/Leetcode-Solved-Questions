class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(num1), len(num2)
        if m>n:
            num1, num2 = num2, num1
        m, n = len(num1), len(num2)
        l, r, half = 0, m-1, (m+n)//2
        while True:
            mid = (l+r)//2
            j = half - mid -2
            num1_left, num2_left, num1_right, num2_right = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid >= 0:
                num1_left = num1[mid]
            if mid+1 < m:
                num1_right = num1[mid+1]
            if j >= 0:
                num2_left = num2[j]
            if j+1 < n:
                num2_right = num2[j+1]
            
            if num1_left <= num2_right and num2_left <= num1_right:
                if (m+n) % 2 == 1:
                    return min(num1_right, num2_right)
                return (min(num1_right, num2_right)+max(num1_left, num2_left))/float(2)
            
            if num1_left > num2_right:
                r = mid - 1
            else:
                l = mid + 1
                
                
        
        