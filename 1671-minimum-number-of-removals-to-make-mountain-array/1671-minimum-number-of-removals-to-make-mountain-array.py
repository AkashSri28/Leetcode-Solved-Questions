class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Step 1: Compute LIS ending at each index
        inc = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    inc[i] = max(inc[i], inc[j] + 1)

        # Step 2: Compute LDS starting at each index
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    dec[i] = max(dec[i], dec[j] + 1)

        # Step 3: Find the longest bitonic subsequence
        max_bitonic_length = 0
        for i in range(1, n - 1):  # The peak cannot be the first or last element
            if inc[i] > 1 and dec[i] > 1:  # Valid peak
                max_bitonic_length = max(max_bitonic_length, inc[i] + dec[i] - 1)

        # Step 4: Minimum removals to make a mountain array
        return n - max_bitonic_length
        
#         n = len(nums)
#         dp_left = [-1]*n
#         dp_right = [-1]*n
#         ans = float('inf')
        
#         def find_max_left(i):
#             if i == 0:
#                 return 0
#             if dp_left[i] == -1:
#                 res = 0
#                 for j in range(i-1, -1, -1):
#                     if nums[j] < nums[i]:
#                         res = max(res, 1+find_max_left(j))
#                 dp_left[i] = res
#             return dp_left[i]
        
#         def find_max_right(i):
#             if i == n-1:
#                 return 0
#             if dp_right[i] == -1:
#                 res = 0
#                 for j in range(i+1, n):
#                     if nums[j] < nums[i]:
#                         res = max(res, 1+find_max_right(j))
#                 dp_right[i] = res
#             return dp_right[i]
        
#         for i in range(n):
#             left = find_max_left(i)
#             right = find_max_right(i)
#             height = 1+left+right
#             if 0 < i < n-1:
#                 ans = min(ans, n-height)
            
#         return ans
            
        