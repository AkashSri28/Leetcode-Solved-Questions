class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            a, b = str(a), str(b)
            return -1 if a+b > b+a else 1

        nums.sort(key=cmp_to_key(compare))
        if nums[0] == 0:
            return '0'
        return ''.join(map(str, nums))

        