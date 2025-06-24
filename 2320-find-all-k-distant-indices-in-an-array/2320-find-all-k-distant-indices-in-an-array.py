class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        # temp = [0]*n

        # def mark(index):
        #     left = max(0, index-k)
        #     right = min(n, index+k+1)
        #     for i in range(left, right):
        #         temp[i] = 1

        # for index, num in enumerate(nums):
        #     if num == key:
        #         mark(index)

        # ans = []
        # for i in range(n):
        #     if temp[i] == 1:
        #         ans.append(i)
        
        # return ans
        ans = []
        r = 0

        for i in range(n):
            if nums[i] == key:
                left = max(r, i-k)
                r = min(n, i+k+1)
                for j in range(left, r):
                    ans.append(j)

        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: From left check for key, take 2 pointers to mark start and end pointers