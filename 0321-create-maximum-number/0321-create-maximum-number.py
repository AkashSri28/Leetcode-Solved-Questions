class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxSubsequence(nums, t):
            stack = []
            drop = len(nums) - t
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(seq1, seq2):
            res = []
            while seq1 or seq2:
                if seq1 > seq2:
                    res.append(seq1.pop(0))
                else:
                    res.append(seq2.pop(0))
            return res

        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = getMaxSubsequence(nums1, i)
            part2 = getMaxSubsequence(nums2, k - i)
            merged = merge(part1[:], part2[:])
            max_result = max(max_result, merged)
        return max_result
