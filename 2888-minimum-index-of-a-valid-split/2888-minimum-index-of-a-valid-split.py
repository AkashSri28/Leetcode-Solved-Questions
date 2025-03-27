class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        def find_max_freq(nums):
            counter = Counter(nums)
            num, count = max(counter.items(), key = lambda x:x[1])
            return num, count

        num, count = find_max_freq(nums)
        left, left_total, right, right_total = 0, 0, len(nums), count*2
        for i, n in enumerate(nums):
            if n == num:
                left_total += 2
                right_total -= 2
            
            left += 1
            right -= 1

            if left_total > left and right_total > right:
                return i

        return -1



        