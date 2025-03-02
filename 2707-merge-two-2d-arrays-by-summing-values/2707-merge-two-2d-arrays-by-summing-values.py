class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] > nums2[j][0]:
                ans.append([nums2[j][0], nums2[j][1]])
                j += 1
            else:
                ans.append([nums1[i][0], nums1[i][1]])
                i += 1

        while i < len(nums1):
            ans.append([nums1[i][0], nums1[i][1]])
            i += 1
        
        while j < len(nums2):
            ans.append([nums2[j][0], nums2[j][1]])
            j += 1

        return ans

        # TC: O(m+n)
        # SC: O(1)
        # Approach: Similar to creating 1 sorted array from 2 sorted arrays
        