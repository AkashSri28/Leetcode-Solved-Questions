class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        curr = sorted(nums)

        def virtual_index(i):
            return (1+2*i)%(n|1)

        for i in range(n):
            nums[virtual_index(i)] = curr[n-1-i]



        

        